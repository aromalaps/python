# find the second largest number and second minimal number using whileloop ?
lis=[10,30,4,5,6]
x=0
while x<len(lis):
    if lis[x]==max(lis):
      lis.pop(x)
      print("second largest",max(lis))
    if lis[x]==min(lis):
       lis.pop(x)
       print("second smallest",min(lis))
    x+=1