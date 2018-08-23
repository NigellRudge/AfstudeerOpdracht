import time

class Road:
    """
        This class represent a Road in the simulation
    """   
    def __init__(self, name, image_source):
        self.name = name
        self.image_src = image_source
        self.num_cars = 0

    def UpdateCount(self,amount):
        self.count = amount
    
    def ClearCount(self):
        self.count = 0 
    
    def __str__(self):
        return str(self.__class__) +  " : " + str(self.__dict__)
    
    def carDriveUp(self, car_number):
        time.sleep(1)
        print("car " + str(car_number + 1) +" now driving")
        time.sleep(0.5)
    
    def setImage(self, image_path):
        self.image_src = image_path