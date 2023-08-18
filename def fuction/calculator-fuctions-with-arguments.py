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
if i=="add":
    add(10,20)
elif i=="sub":
    sub(10,20)
elif i=="mul":
    mul(10,20)
else:
    div(10,20)
     