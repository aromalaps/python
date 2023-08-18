# write a program that takes an integer as input and 
# prints the number of digits in that number using a while loop?
list=[]
user=int(input("enter a value"))
y=0
user=str(user)
while y<len(user):
    list.append(user[y])
    y+=1
print(list)
print(len(list))