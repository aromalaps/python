# write a program to check if a given number is prime or not using a for loop?
# num=2
# if num<1:
#    print("it is not a prime number")
# else:
#  for i in range(2,num):
#    if num%i==0:
#      print("it is not a prime number")
#      break
#    else:
#      print("it is a prime number")
#      break
# if num==2:
#print("it is a prime number") 
num=12
count=0
if num<1:
    print("it is not a prime number")
else:
    for i in range(2,num+1):
        if num%i==0:
          count+=1
if count>1:          
  print("it is not a prime number")
else:
   print("it is a prime number")