x=int(input("enter a number"))
count=1
for i in range(x,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()