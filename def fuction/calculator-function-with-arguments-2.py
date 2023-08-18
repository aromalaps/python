def add(a,b):
    sum=a+b
    print(sum)
def sub(a,b):
    sum=a-b
    print(sum)
def mul(a,b):
    sum=a*b
    print(sum)
def div(a,b):
    sum=a/b
    print(sum)
i=input("enter :-add/sub/mul/div")
a=int(input("enter a number"))
b=int(input("enter a number"))
if i=="add":
    add(a,b)
elif i=="sub":
    sub(a,b)
elif i=="mul":
    mul(a,b)
else:
    div(a,b)