# 2) Create a class Person with a constructor that takes a name argument and stores 
# it in an instance variable. Create a class CanCook with a method cook() that 
# doesn't do anything. Create a class CanPaint with a method paint() that 
#  doesn't do anything. Create a subclass Chef that inherits from Person, CanCook, 
# and CanPaint and has a constructor that takes a specialty argument and stores it in
# an instance variable
class Person:
    def __init__(self,name):
        self.name=name
        print("name is ",name)
class cook:
    def cook(self):
        print("coook food")
class Canpaint:
    def paint(self):
        print("can paint")
class Chef(Person,cook,Canpaint):
    def __init__(self,speciality):
        self.speciality=speciality
        print("specality",speciality)
obj=Person("aromal")
obj1=Chef("he can do both")
obj1.cook()
obj1.paint()