total=int(input("enter the purchase amount"))
if total>100:
    print("you are eligible for the discount amount")
    pay= (total*10)/100
    amount=total-pay
    print("payable amount =",amount)
elif total<100:
    print("you are not eligible for the discount amount")
    print("discount is applied only purchase above $100")
    print("payable amount =",total)