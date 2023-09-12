# 1) Create a class Animal with a constructor that takes a name argument and stores 
# it in an instance variable. Create a class CanFly with a method fly() that doesn't 
# do anything. Create a class CanSwim with a method swim() that doesn't 
# do anything. Create a subclass Duck that inherits from Animal, CanFly, and 
# CanSwim and has a constructor that takes a color argument and stores it in an 
# instance variable.
class Animal:
    def __init__(self,name):
        self.name=name
        print("it is a ",name)
class CanFly:
    def fly(self):
        print("it can fly")
class CanSwim:
    def swim(self):
        print("it can swim")
class Duck(Animal,CanFly,CanSwim):
    def __init__(self,color):
        self.color=color
        print("color is ",color)
obj=Duck("red")
obj1=Animal("duck")
obj.fly()
obj.swim()