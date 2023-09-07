list=[3,11,12,9,17]
user=int(input("enter the locker"))
user1=int(input("enter the next locker"))
list2=list[::2]
list3=list[1::2]
if user and user1 in list2 :
    for i in list:
        if user==i:
            print(" ")
elif user and user1 in list3:
    print(user,user1)
    theft=user+user1
    print("total amount theft=",theft)
