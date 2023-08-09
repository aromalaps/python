end=int(input("enter a value"))
pattern="*"
space=" "
count=1
inc=0
h=end
print((space*end)*1,pattern*count)
for i in range(1,end+1):
    end-=1
    print(space*end,pattern,space*inc,pattern,space*end)
    inc+=2
print((pattern+space*2)*h)