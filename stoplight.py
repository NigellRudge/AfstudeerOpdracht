from sensor import Sensor
from queque import Queue
import time

class Stoplight:
    """
        This class represent the Stoplight that wil regulate the roads
    """
    def __init__(self, road_array):
        self.road_queque = Queue()
        self.road_array = road_array
        self.sensor = Sensor()
        self.position_1 = None
        self.position_2 = None
        self.position_3 = None
        self.position_4 = None

        self.stoplight_color = "Red"
        
    def DetectCars(self):

        # if(road_array is not None):
        #     self.road_array = road_array
        for i in range(0, len(self.road_array)):
            self.road_array[i].num_cars = self.sensor.detectCars(self.road_array[i])
            print( "the amount found is: " + str(self.road_array[i].num_cars))
            print("*************************************************")
            self.road_queque.insert(self.road_array[i])
        
        # for road in self.road_array:
        #     if(self.position_1 == None):
        #         self.position_1 = road
        #         continue
        #     if(self.position_1.num_cars < road.num_cars):
        #         self.position_4 = self.position_3
        #         self.position_3 = self.position_2
        #         self.position_2 = self.position_1
        #         self.position_1 = road
        #     if(self.position_2 == None):
        #         self.position_2 = road
        #         continue
        #     if(self.position_2.num_cars < road.num_cars and road.num_cars < self.position_1.num_cars):
        #         self.position_4 = self.position_3
        #         self.position_3 = self.position_2
        #         self.position_2 = road
        #     if(self.position_3 == None):
        #         self.position_3 = road
        #     if(self.position_3.num_cars < road.num_cars and road.num_cars < self.position_2.num_cars):
        #         self.position_4 = self.position_3
        #         self.position_3 = road
        #     else:
        #         self.position_4 = road
        
        # self.Run()
        self.RunFromQueue()

    def ChangeLightColor(self):       
        if self.stoplight_color == "Red" :
            #time.sleep(1.5)
            self.stoplight_color = "Green"
            print("Light turns " + self.stoplight_color)
            
        elif self.stoplight_color == "Green" :
            #time.sleep(1.5)
            self.stoplight_color = "Yellow"
            print("Light turns " + self.stoplight_color)
        else:
           # time.sleep(1.5)
            self.stoplight_color = "Red"
            print("Light turns " + self.stoplight_color)
    
    def Run(self):
        self.PrintInfo(self.position_1)
        self.ChangeLightColor()
        for i in range(0,self.position_1.num_cars):
            self.position_1.carDriveUp(i)
        self.ChangeLightColor()
        self.ChangeLightColor()

        self.PrintInfo(self.position_2)
        self.ChangeLightColor()
        for i in range(0,self.position_2.num_cars):
            self.position_2.carDriveUp(i)
        self.ChangeLightColor()
        self.ChangeLightColor()


        self.PrintInfo(self.position_3)
        self.ChangeLightColor()
        for i in range(0,self.position_3.num_cars):
            self.position_3.carDriveUp(i)
        self.ChangeLightColor()
        self.ChangeLightColor()


        self.PrintInfo(self.position_4)
        self.ChangeLightColor()
        for i in range(0,self.position_4.num_cars):
            self.position_4.carDriveUp(i)
        self.ChangeLightColor()
        self.ChangeLightColor()

    def PrintInfo(self,road):
        print("*************************************************")
        print(str(road.name) + " now in focus")
        print("Total amount of cars is: " + str(road.num_cars))
        print("The current value of the light is: " + self.stoplight_color)
        print("*************************************************")
        #time.sleep(1)
    
    def RunFromQueue(self):
        while self.road_queque.isNotEmpty():
            road = self.road_queque.deQueue()
            self.PrintInfo(road)
            self.ChangeLightColor()
            for i in range(0,road.num_cars):
                road.carDriveUp(i)
            self.ChangeLightColor()
            self.ChangeLightColor()