# write a program that takes a list of integers as input and 
# print the sum of all even numbers in the list using a while loop?
x=5
list=[]
list2=[]
y=0
sum=0
while y<5:
  user=int(input("enter some numbers"))
  list.append(user)
  y+=1
for i in list:
    print(i)
    if i%2==0:
      list2.append(i)
      sum+=i
print("list of elements are",list)
print("even numbers are",list2)
print("sum of even numbers are ",sum)