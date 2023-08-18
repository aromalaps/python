#write a program that takes a string input from the user and uses a for loop to count the occurances of each character in the string.
#print the character and its count.
string=input("enter a string to continue")
dict={}
for i in string:
    if i not in dict:
      count=1
      dict[i]=count
    else:
       count+=1
       dict[i]=count
print(dict)
