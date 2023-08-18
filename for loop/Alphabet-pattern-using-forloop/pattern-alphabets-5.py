#        A
#      A B C
#    A B C D E
#  A B C D E F G
user=5
count=65
space=" "
c=5
for i in range (1,user+1):
     print(space*(user-1),end="")
     user-=1
     for j in range(i):
         print(chr(count),end=" ")
         count+=1
     print()