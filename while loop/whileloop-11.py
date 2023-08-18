#write a program that takes a list of integrs as input 
#and print the numbers in the  list that are greater than the average of all the numbers using a while loop?
i=0
j=5
list=[]
k=0
sum=0
while i in range(j+1):
    user=int(input("enter a number"))
    list.append(user)
    i+=1
    while k<len(list):
        sum+=list[k]
        k+=1
av=sum//(len(list)+1)
if av>max(list):
  print(av,"is the average of list is")
else:
   print(max(list),"greater than average")