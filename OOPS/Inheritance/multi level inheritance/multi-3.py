class Person:
    def per(self,name,age):
        print("name is  :",name)
        print("Age is   :",age)
class Employee(Person):
    def emp(self,salary):
        print("salary is:",salary)
class Manager(Employee):
    def __init__(self,department):
        self.department=department
        print("Department is :",department)
obj1=Manager("python")
obj1.per("Aromal",21)
obj1.emp(20000)