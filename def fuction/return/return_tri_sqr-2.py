# Write a function  named sum_of_squares that takes an integer n as an argument 
# and returns the sum of the squares of all integers from 1 to n.?
def sum_of_squares(sum,input):
    for i in range(1,input+1):
        sum+=i*i
        print(sum)
    return sum
s=sum_of_squares(0,4)
print(s)
