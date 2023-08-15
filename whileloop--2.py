#write a program that 
user1=6
user2=12
s=0
i=1
if user1<user2:
    store=user1
else:
    store=user2
while i<=store:
    if user1%i==0 and user2%i==0:
        s=i
    i+=1
print("the greatest divisor is ",s)