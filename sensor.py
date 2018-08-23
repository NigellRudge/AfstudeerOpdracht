import tensorflow as tf
import numpy as np 
import matplotlib
import sys
import os
import cv2
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from matplotlib import pyplot as plt

class Sensor:

    def __init__(self):
        MODEL_NAME = "faster_rcnn_inception_v2_coco_2018_01_28"
        self.PATH_TO_FROZEN_GRAPH = os.path.join(os.getcwd(),"object_detection",MODEL_NAME ,"frozen_inference_graph.pb")
        PATH_TO_LABELS = os.path.join(os.getcwd(),"object_detection" ,"data","mscoco_label_map.pbtxt")
        NUM_CLASSES = 90
        
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(categories)
        
        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_FROZEN_GRAPH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        config = tf.ConfigProto()
        config.intra_op_parallelism_threads = 22
        config.inter_op_parallelism_threads = 22
        self.sess = tf.Session(graph=self.detection_graph,config=config)        

        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')    
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def detectCars(self,Road):
        PATH_TO_VIDEO = os.path.join(os.getcwd(),"images",Road.image_src)
        frame = cv2.imread(PATH_TO_VIDEO)
        resized_frame = cv2.resize(frame,(840,480)) 
        frame_expanded = np.expand_dims(resized_frame, axis=0)

        (boxes, scores, classes, num) = self.sess.run(
                [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
                feed_dict={self.image_tensor: frame_expanded})
                
        # vis_util.visualize_boxes_and_labels_on_image_array(
        #     resized_frame,
        #     np.squeeze(boxes),
        #     np.squeeze(classes).astype(np.int32),
        #     np.squeeze(scores),
        #     self.category_index,
        #     use_normalized_coordinates=True,
        #     line_thickness=8,
        #     min_score_thresh=0.80)
            
        # cv2.imshow(Road.name,resized_frame)
        # cv2.waitKey(0)
        final_score = np.squeeze(scores)
        count = 0
        for i in range(100):
            if scores is None or final_score[i] > 0.75:
                count = count + 1
        print("*************************************************")
        print("Detection on Road: " + Road.name + " complete")
        print("Detected " + str(count) + " amount of cars")
        return count