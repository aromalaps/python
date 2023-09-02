def sample(fact):
    if fact==1:
        return fact
    return fact * sample(fact-1) 
s=sample(5) 
print(s)
