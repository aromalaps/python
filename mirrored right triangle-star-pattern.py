pat="*"
s=" "
count=9
star=1
for i in range(1,10):
    print(s*count,pat*star)
    count-=1
    star+=1
