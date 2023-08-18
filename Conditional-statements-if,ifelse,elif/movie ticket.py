age=int(input("enter the age"))
day=input("enter the week ")
if age>12 and age<18 and day=="wednesday":
    print("the ticket cost is $4")
elif age<12 or age>65 :
    print("ticket cost is $5")
else:
    print("the ticket cost is $8")