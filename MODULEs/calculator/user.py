import calcualtion as calcu
a=int(input("enter a number"))
b=int(input("enter a number"))
user=input("enter add for addition enter sub for substraction enter mul for multiplication enter div for division")
if user=="add":
    calcu.ob.add(a,b)
elif user=="sub":
    calcu.ob.sub(a,b)
elif user=="mul":
    calcu.ob.mul(a,b)
elif user=="div":
    calcu.ob.div(a,b)
calcu.ob.name
print(calcu.ob.name)