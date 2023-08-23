#multiplication table using while loop
x=10
y=1
def mul(user):
    sum=user*y
    print(user,"*",y,"=",sum)
use=int(input("enter a value"))
while y<=x:
    mul(use)
    y+=1