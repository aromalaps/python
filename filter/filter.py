# filter all the positive integers in the list by using filter() function?
lis=[1,2,3,4,-3]
x=filter(lambda a:a>0,lis)
y=list(x)
print(y)