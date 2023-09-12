# Multi Level Inheritance Questions
# 1) Create a class Person with a constructor that takes a name and age argument and 
# stores them in instance variables. Create a subclass Employee that inherits from 
# Person and has a constructor that takes a salary argument and stores 
#  it in an instance variable. Create a subclass Manager that inherits from 
# Employee and has a constructor that takes a department argument and stores it in an
# instance variable.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("name is  :",name)
        print("Age is   :",age)
class Employee(Person):
    def __init__(self,salary):
        self.salary=salary
        print("salary is:",salary)
class Manager(Employee):
    def __init__(self,department):
        self.department=department
        print("Department is :",department)
obj1=Person("Aromal",21)
obj2=Employee(2000)
obj3=Manager("python")
