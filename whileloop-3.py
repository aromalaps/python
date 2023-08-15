# palindrome or not
user=int(input("enter a number"))
y=0
list=[]
s=str(user)
while y<len(s):
    list.append(s[y])
    y+=1
reverse=list[::-1]
print(reverse)
if reverse==list:
    print("it is a palindrome")
else:
    print("it is not a palindrome")