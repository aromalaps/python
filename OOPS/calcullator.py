a=int(input("enter a number"))
b=int(input("enter a number"))
user=input("enter add for addition enter sub for substraction enter mul for multiplication enter div for division")
class calculator:
    def add(self,input1,input2):
        sum = input1 + input2
        print(sum)
    def sub(self,input1,input2):
        sum = input1 - input2
        print(sum)
    def mul(self,input1,input2):
        sum = input1 * input2
        print(sum)
    def div(self,input1,input2):
        sum = input1 / input2
        print(sum)
ob=calculator()
if user=="add":
    ob.add(a,b)
elif user=="sub":
    ob.sub(a,b)
elif user=="mul":
    ob.mul(a,b)
elif user=="div":
    ob.div(a,b)