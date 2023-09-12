# 4) Create a parent class called "Person" with attributes "name" and "age". Create a
# child class called "Student" that inherits from "Person" and has an additional 
# attribute "grade".
class Person:
    def sample(self,name,age):
        print("name is :",name)
        print("age is  :",age)
class Student(Person):
    def sample1(self,grade):
        print("grade is:",grade)
obj=Student()
obj.sample("aromal",21)
obj.sample1("A grade")