# Extend the 'Person class from the previous question by adding a method `greet` that prints a greeting message with
# the person's name.Create an instance and call this method.
# class person:
#     def greet(self):
class person:
    name="python"
    age=3
    def greet(self):
        print(self.name,"  i have a greeting")
    def sample(self):
        print(self.age)
obj=person()
obj.greet()
obj.sample()