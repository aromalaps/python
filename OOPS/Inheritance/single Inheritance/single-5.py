# 5) Create a parent class called "Animal" with attributes "species" and "legs". 
#Create a child class called "Cat" that inherits from "Animal" and has an additional
# attribute "color".
class Animal:
    def sample(self,species,legs):
        print("Animal species is      :",species)
        print("The animal have 4 legs :",legs)
class Cat(Animal):
    def sample1(self,color):
        print("color is :",color)
obj=Cat()
obj.sample("Cat",4)
obj.sample1("Snowy white")