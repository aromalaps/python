#Takes a sentence as an input and print only the word start with upper character?
sent=input("enter a string to continue")
li=sent.split()
print(li)
list=[]
a=""
for i in li:
     print(i)
     if i[0].isupper():
         list.append(i)
         a+=i
print(list)
print(a)
