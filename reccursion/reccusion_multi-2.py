def funct(user,end,output):
    if user<end:
        user=user*output
        user+=1
        output+=user
    return user
out=1
u=5
e=10
s=funct(u,e,out)
print(s)
# int(input("enter a value"))
# odd number print 1 to 10
# even number print 1 to 10