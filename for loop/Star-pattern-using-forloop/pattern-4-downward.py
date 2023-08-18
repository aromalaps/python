pat="*"
end=int(input("enter a number"))
count=end
spac=" "
sp=1
for i in range(1,end):
    print(spac*sp,pat*count)
    sp+=1
    count-=2