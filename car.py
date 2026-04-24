class car():
    def __init__(self,cost,brand,color):
        self.a=cost
        self.b=brand
        self.c=color
        print("details of car!")
    def details(self):
            print(f"cost:{self.a}")
            print(f"brand:{self.b}")
            print(f"color:{self.c}")
my_car=car("1000000000","bmw","black")
my_car.details()