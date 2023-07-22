#palindrome or not
string=input("enter a sting")
print("the entered string is ",string)
rev=string[::-1]
print("reversed=",rev)
if string==rev:
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
