#write a program that takes a string input from the user and uses a for loop to count the occurances of each character in the string.
#print the character and its count.
string="hello"
dict={}
for i in string:
    print(i)
    if i not in dict:
      count=1
      dict.update({count:i})
      print(dict)
    else:
       count+=1
       dict.update({count:i})
       print(dict)
       
     
