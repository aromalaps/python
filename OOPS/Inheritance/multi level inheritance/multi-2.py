# 2) Create a class Shape with a constructor that takes a color argument and stores 
# it in an instance variable. Create a subclass Rectangle that inherits from Shape 
# and has a constructor that takes width and height arguments and stores
#  them in instance variables. Create a subclass Square that inherits from 
# Rectangle and has a constructor that takes a side argument and sets the width and 
# height instance variables to the value of side.
class Shape:
    def __init__(self,color):
        self.color=color
        print("color is :",color)
class Rectangle(Shape):
    def __init__(self,width,height):
       self.width=width
       self.height=height
       print("rectangle")
       print("width = ",width)
       print("height = ",height)
class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        self.width=side
        self.height=side
        print("side of the square = ", side)
obj=Shape("red")
obj1=Rectangle(20,30)
obj2=Square(20)