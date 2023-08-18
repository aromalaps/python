products={"shirt":500,"jeans":700,"panties":100,"shorts":250}
countof={1,2,3,4,5,6,7,8,9,10}
list=[]
sum=0
while True:
    print("enter the product you want to purchase:-")
    purchase=input("enter the product to continue")
    if purchase not in products:
         print("please enter a product in stock")
    else:
        count=int(input("how many do you want"))
        if count in countof:
            print("you have purchased :-",count,purchase)
            sum+=(count*products[purchase])
            quit_continue_complete=input("[if you want to continue purchasing enter c to continue]""[enter q to exit]"" [if you want to complete purchase enter Y]")
            if quit_continue_complete=="q":
                break
            elif quit_continue_complete=="y":
                print("your total purchase=",sum)
                if sum>2000:
                    discount=500
                    print("now you are eligible for your discount")
                    sum-=500
                    print("payable amount=",sum)
                    break
                else:
                    break
            else:
                continue
