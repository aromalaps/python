# find all the sum of even numbers from 1 to 100 using for loop?
sum=0
for i in range(1,100):
    if i%2==0:
     print(i)
     sum=sum + i
print(sum)