def sample(l):
    return l%2==0
l=[1,2,3,4,5,6]
f=filter(sample,l)
print(f)
print(list(f))
print(tuple(f))
print(set(f))