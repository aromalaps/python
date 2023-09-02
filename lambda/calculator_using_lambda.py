
v=lambda a,b:a*b
x=lambda a,b:a+b
y=lambda a,b:a-b
z=lambda a,b:a/b
user=int(input("enter a value"))
user1=int(input("enter a value")) 
user=input("enter 'add' for additon 'sub' for substaction enter 'mul' for multiplication enter 'div' for division")
if user=="add":
    print(x(user,user1))
elif user=="sub":
    print(y(user,user1))
elif user=="mul":
    print(v(user,user1))
elif user=="div":
    print(z(user,user1))