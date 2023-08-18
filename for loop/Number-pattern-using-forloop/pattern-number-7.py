# 3
# 3 8
# 3 8 3
# 3 8 3 8
n=3
m=8
user=5
for i in range(1,user+1):
    for j in range(i):
        if j%2==0:
            print(n,end=" ")
        else:
            print(m,end=" ")
    print()
