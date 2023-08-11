# imp
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
n=1
m=0
user=int(input("enter a value"))
for i in range(1,user+1):
    for j in range(i):
        if j%2==0:
            print(n,end=" ")
        else:
            print(m,end=" ")
    print()

