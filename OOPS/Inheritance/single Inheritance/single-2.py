# 2) Create a parent class called "Employee" with attributes "name" and "salary". 
# Create a child class called "Manager" that inherits from "Employee" and has an 
# additional attribute "department". 
class Employee:
    def detail(self,name,salary):
        print("name is   :",name)
        print("salary is :",salary)
class Manager(Employee):
    def dep(self,department):
        print("department is :",department)
obj=Manager()
obj.detail("aromal",20000)
obj.dep("python ")