#write a program that takes a sentence as an input and print the longest word in the sentence?
b=0
sentence=input("enter some sentence")
list=sentence.split()
print(list)
long=""
for i in list:
    a=len(i)
    if a>b:
      b=a
      long=i
print("longest is",long)