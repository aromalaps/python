# def funct(factorial,input):
#     if input>0
#         factorial*=input
#         return factorial * funct(factorial,input-1)
# s=funct(1,3) 
# print(s)

def sample(fact):
    if fact==1:
        return fact 
    return fact * sample(fact-1) 
s=sample(3) 
print(s)