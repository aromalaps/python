# 1) Create a parent class called "Vehicle" with a method "start_engine" that prints 
# out "The engine is starting". Create a child class called "Car" that inherits from 
# "Vehicle" and has an additional method "drive" that prints out 
#  "The car is driving".
class Vehicle:
    def start_engine(self):
        print("the engine is starting")
class Car(Vehicle):
    def drive(self):
        print("the car is driving")
obj=Car()
obj.start_engine()
obj.drive()