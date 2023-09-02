# use a lambda function to filter out even numbers from a list of integers?
def sample(lis):
   return lis%2==0
li=[1,2,3,4,5,6]
f=filter(sample,li)
print(list(f))