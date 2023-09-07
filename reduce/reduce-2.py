from functools import reduce
def sample(a,b):
        return a+b
lis=[1,2,3,4,5,6]
f=filter(lambda a:a%3==0,lis)
y=list(f)
x=reduce(sample,y)
print(x)