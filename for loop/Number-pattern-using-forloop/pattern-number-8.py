# 5 
# 5 3
# 5 3 5
# 5 3 5 3
# 5 3 5 3 5
n=3
m=5
user=5
for i in range(1,user+1):
    for j in range(i):
        if j%2==0:
            print(m,end=" ")
        else:
            print(n,end=" ")
    print()        