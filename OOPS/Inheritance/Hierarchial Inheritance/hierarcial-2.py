# 2) Create a class Device that has instance variables name and price, and a method 
# turn_on() that prints a message indicating that the device is turning on. 
# Create  subclasses Phone and Tablet that inherit from Device and add 
#  a method make_call() to Phone and a method browse_internet() to Tablet. Create 
# objects of the Phone and Tablet classes and call their turn_on(), make_call(), and 
# browse_internet() methods.
class Device:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def turn_on(self):
        print("indicating that the device is turning on")
class Phone(Device):
    def make_call(self):
        print("you can make a call")
class Tablet(Device):
    def browse_internet(self):
        print("you can brower on tablet")
obj=Device("tablet",2000)
obj.turn_on()
obj1=Phone("abc",123)
Obj2=Tablet("abc",123)
obj1.make_call()
Obj2.browse_internet()
