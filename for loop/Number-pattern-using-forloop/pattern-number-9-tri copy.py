#pattern triangle using numbers
#    1
#   1 2
#  1 2 3
# 1 2 3 4 
#1 2 3 4 5 
num=5
count=1
for i in range(1,num+1):
  print(" "*(num-1),end="")
  num-=1
  for j in range(1,i+1):
        print(j,end=" ")
  print( )