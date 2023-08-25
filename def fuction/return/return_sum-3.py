# Write a function named median_of_list that takes a list of numbers as an argument
# and returns the median value.?
li=[1,2,3,4,5,6]
def median_of_list(list):
    length=len(li)
    median=(length+1)/2
    return median
sum=median_of_list(li)
print(sum)