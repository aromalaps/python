user="535"
list=[]
for i in user:
    list.append(i)
reverse=list[::-1]
print(reverse)
if reverse==list:
    print("it is a palindrome")
else:
    print("it is not a palindrome")