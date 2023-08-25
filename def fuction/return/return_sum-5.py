# Write a function named digit_sum that takes an integer as an argument and 
# returns the sum of its digits?
input="123"
def digit_sum(ins):
  sum=0
  for i in ins:
    x=int(i)
    sum+=x
  return sum
print(digit_sum(input))