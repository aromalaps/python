#write a program that takes a list of integers from the user,
#and uses a for loop to create a new list containing only the duplicate elements from the original list.
lis=input("enter some integers")
print(lis)
lis1=lis.split()
print(lis1)
li=[]
lisi=[]
for i in lis1:
    if i not in li:
       li.append(i)
    else:
        lisi.append(i)
print("a new list with only duplicate elements",lisi)