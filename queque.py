
class Queue:
    def __init__(self):
        self.road_array = []
    
    def insert(self, new_element):
        self.road_array.append(new_element)
        self.road_array = sorted(self.road_array,key = lambda road:road.num_cars)
    
    def deQueue(self):
        return self.road_array.pop(0)
    
    def print(self):
        for road in self.road_array:
            print(road)
        print("***********")   
    
    def isEmpty(self):
        return len(self.road_array) == 0
    
    def isNotEmpty(self):
        return len(self.road_array) > 0
