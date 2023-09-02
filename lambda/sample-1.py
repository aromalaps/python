#write a python program to create a lambda function that adds 15 to a given number passed in as an arguments 
#also create a lambda function that multiplies argument 'x' with argument 'y' and prints the result.
x=lambda a:a+15
y=lambda c,d:c*d
user=int(input("enter a value"))
print(x(user))
user1=int(input("enter a value"))
print(y(user,user1))