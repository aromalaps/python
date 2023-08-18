#write a program that takes a list of integers as input and prints the number of even number 
#and the number of odd numbers in the list using a while loop.
i=0
x=5
list=[]
while i in range(5):
    user=int(input("enter an integer"))
    list.append(user)
    i+=1
odd=[]
even=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
odd_length=len(odd)
even_length=len(even)
print("count of even numbers",even_length)
print("count of odd numbers are",odd_length)