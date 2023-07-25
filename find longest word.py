#write a program that takes a sentence as an input and print the longest word in the sentence?
sentence=input("enter some sentence")
list=sentence.split()
print(list)
li=[]
for i in list:
    a=len(i)
    print(a)
    li.append(a)
print(li)
for j in li:
    print()