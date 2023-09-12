# 3) Create a class Person that has instance variables name and age, and a method 
# speak() that prints a message indicating that the person is speaking. Create 
# subclasses Student and Teacher that inherit from Person and add a method
#  study() to Student and a method teach() to Teacher. Create objects of the 
# Student and Teacher classes and call their speak(), study(), and teach() methods.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name is",name,"age is :",age)
    def speak(self):
        print("the person is speaking")
class Student(Person):
    def study(self):
        print("student is studing")
class Teacher(Person):
    def teach(self):
        print("teacher teaches the student")
obj=Person("aromal",20)
obj1=Student("abc",21)
obj2=Teacher("abc",21)
obj.speak()
obj1.study()
obj2.teach()