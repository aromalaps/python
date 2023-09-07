from functools import reduce
lis=[1,2,3,4,5,6]
f=filter(lambda a:a%3==0,lis)
y=list(f)
x=reduce(lambda a,b:a+b,y)
print(x)