# Rectangle Class:
# Define a class called 'Rectangle with an `_init_ ` method that initializes the attributes 'length' and `width`.
# Add a method calculate_area` that calculates and returns the area of the rectangle.
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        area=self.length*self.width
        print(area)
obj=rectangle(10,20)
obj.calculate_area()