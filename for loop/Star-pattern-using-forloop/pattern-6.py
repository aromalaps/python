end=int(input("enter a value"))
pattern="*"
space=" "
count=1
inc=0
en=end
print(end*space,pattern*count)
for i in range(1,end):
    end-=1
    print(space*end,pattern,space*inc,pattern,space*end)
    inc+=2
cou=1
inc-=2
for i in range(1,en):
    print(space*cou,pattern,space*inc,pattern,space*cou)
    cou+=1
    inc-=2
print(en*space,pattern*count)