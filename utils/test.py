import time

class Road:
    """
        This class represent a Road in the simulation
    """   
    def __init__(self, name, count):
        self.name = name
        self.num_cars = count

    def UpdateCount(self,amount):
        self.count = amount
    
    def ClearCount(self):
        self.count = 0 
    
    def __str__(self):
        return  str(self.__dict__)
    
    def __repr__(self):
        return repr((self.name,self.num_cars))

    def carDriveUp(self, car_number):
        time.sleep(1)
        print("car " + str(car_number) +" now driving")
        time.sleep(0.5)
    


roadA = Road("road1",20)
roadB = Road("road2",15)
roadC = Road("road3",30)
roadD = Road("road4",25)
students = [
    roadA,roadB,roadC,roadD
]

print(students)
sorted_students = sorted(students,key=lambda road:road.num_cars)
print(sorted_students)
print(students.pop())