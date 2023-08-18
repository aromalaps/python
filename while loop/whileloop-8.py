# write a program that takes a list of integers as input and
# prints the sum of all the numbers that are divisible by 3 or 5 using a while loop?
y=0
list=[]
sum=0
lis2=[]
while y<5:
    user=int(input("enter a number"))
    y+=1
    list.append(user)
for i in list:
    if i%3==0 or i%5==0:
        sum+=i
print(sum)