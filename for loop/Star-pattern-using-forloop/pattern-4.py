#    *
#   ***
#  *****
# *******
pat="*"
count=1
spac=" "
ab=int(input("enter a value"))
sp=ab
for i in range(1,ab+1):
    print(spac*sp,pat*count)
    count+=2
    sp-=1