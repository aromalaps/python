# 3) Create a parent class called "Shape" with attributes "color" and "size". Create 
# a child class called "Circle" that inherits from "Shape" and has an additional 
# attribute "radius".
class shape:
    def att(self,color,size):
        print("color of the circle is :",color)
        print("size of the circle is  :",size)
class Circle(shape):
    def att1(self,radious):
        print("radious of the circle is :",radious)
obj=Circle()
obj.att("Red","size=2*r")
obj.att1("r=C/2π")