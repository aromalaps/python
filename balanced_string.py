# balanced string in python  using a and b
user=input("enter a string with a and b")
count=0
count1=0
for i in input:
    if i=="a":
        count+=1
    elif i=="b":
        count1+=1
    else:
        continue
if count1==count:
    print("balanced string")
else:
    print("unbalanced string")
    print("a=",count,"b=",count1)