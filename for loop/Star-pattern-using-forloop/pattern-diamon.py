patt="*"
end=int(input("enter a value"))
space=" "
sp=end
count=1
for i in range(1,end):
    print(space*sp,patt*count)
    count+=2
    sp-=1
sp=2
for i in range(1,end):
    count-=2
    print(space*sp,patt*count)
    sp+=1