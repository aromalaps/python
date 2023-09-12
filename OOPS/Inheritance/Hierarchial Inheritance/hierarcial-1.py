# Hierarchial Inheritance Questions
# 1) Create a class Vehicle with instance variables brand and model, and a method 
# start_engine() that prints a message that the engine has started.
# Create a class Car that also inherits from Vehicle and has additional instance
# variables color and seats, and a method drive() that prints a message that the 
# car is being driven. 
# Create a class Bike that also inherits from Vehicle and has 
# additional instance variables color and type, and a method ride()
# that prints a message that the bike is being ridden. Create objects of both Car 
# and Bike classes and call their respective methods.
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print("brand      :",brand)
        print("The model  :",model)
    def start_engine(self):
         print(" the engine has started")
class Car(Vehicle):
    def __init__(self,color,seats):
        self.color=color
        self.seats=seats
        print("color      :",color)
        print("seats      :",4)
    def drive(self):
        print(" the car is being driven")
class Bike (Vehicle):
    def __init__(self,color,type):
        self.color=color
        self.type=type
        print("color      : ",color)
        print("type       :",type)
    def ride(self):
         print("the bike is being ridden")
obj=Vehicle("Yamaha",3.1)
obj1=Car("red",4)
obj1.start_engine()
obj1.drive()
obj=Vehicle("Yamaha",3.1)
obj2=Bike("blue","R1")
obj2.start_engine()
obj2.ride()