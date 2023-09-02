def sample(l):
    return l**2
l=[1,2,3,4,5,6]
f= map(sample,l)
print(f)
print(list(f))
#p=list(map(lambda n:n**2,l))
#print(p)