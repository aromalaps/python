#write a program that takes a string input from the user and uses a for loop to count the number of vowels(a,e,i,o,u)in the string
#ignore case while counting
string=input("enter a string")
list=['a','e','i','o','u']
lis=[]
for i in string:
    if i in list:
        lis.append(i)
        li=len(lis)
print(lis)
print("number of vowels in this string",li)