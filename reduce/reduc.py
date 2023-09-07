from functools import reduce
def func(a,b):
    return a*b
lis=[1,2,3,4,5,6]
print(reduce(func,lis))