from road import Road
from stoplight import Stoplight

class Program:
    
    def __init__(self,stoplight,road_array):
        self.stoplight = stoplight
        self.road_array = road_array
    
    def situationOne(self):
        situation_one_images = [
                "image1","image2","image3","image4",
        ]
        count = 0
        while count < len(self.road_array):
            self.road_array[count].setImage(situation_one_images[count])
            count = count + 1
        print("*************************************************")
        print("SITUATION ONE: NOW DETECTING CARS")
        self.stoplight.DetectCars(self.road_array)
        print("*************************************************")

    def situationTwo(self):    
        situation_two_images = [
            "image5","image6","image7","image8",
        ] 
        count = 0
        while count < len(self.road_array):
            self.road_array[count].setImage(situation_two_images[count])
            count = count + 1
        print("*************************************************")
        print("SITUATION TWO: NOW DETECTING CARS")
        self.stoplight.DetectCars(self.road_array)
        print("*************************************************")

    def situationThree(self):
        situation_three_images = [
            "image9","image10","image11","image12",
        ]
        count = 0
        while count < len(self.road_array):
            self.road_array[count].setImage(situation_three_images[count])
            count = count + 1
        print("*************************************************")
        print("SITUATION THREE: NOW DETECTING CARS")
        self.stoplight.DetectCars(self.road_array)
        print("*************************************************")


    def situationFour(self):
        situation_four_images = [
            "image13","image14","image15","image16",
        ]
        count = 0
        while count < len(self.road_array):
            self.road_array[count].setImage(situation_four_images[count])
            count = count + 1
        print("*************************************************")
        print("SITUATION FOUR: NOW DETECTING CARS")
        self.stoplight.DetectCars(self.road_array)
        print("*************************************************")

    def Run(self):
        self.situationOne()
        self.situationTwo()
        self.situationThree()
        self.situationFour()
        
def main():
    road_1 = Road("Road 1","image7.jpg")
    road_2 = Road("Road 2","image2.jpg")
    road_3 = Road("Road 3","image3.jpg")
    road_4 = Road("Road 4","image5.jpg")
    road_array = [
        road_1,road_2,road_3,road_4
    ]
    stoplight = Stoplight(road_array)
    stoplight.DetectCars()
    print("*************************************************")
if __name__ == '__main__':
    main()