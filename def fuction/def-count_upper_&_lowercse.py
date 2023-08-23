# write a python function that accepts a string 
# and counts the number of uppercase and lower case letters?
# sample string:"The quick Brow Fox"
# Expected Output:
# no of uppercase cahracters : 3
# no of lower case Characters: 12
def alpha(sent):
    count=0
    lower=0
    for i in sent:
      if i.isupper():
         count+=1
      elif i.islower():
         lower+=1
    print("no of uppercase cahracters :",count)
    print("o of lower case Characters :",lower)
sent="The quick Brow Fox"
alpha(sent)