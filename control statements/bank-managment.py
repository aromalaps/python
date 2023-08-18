#BANK MANAGEMENT SYSTEM
#write a program that allows user to perform the following actions.
#0.check the account number is valid or not
#1.Deposit money into their account.
#2.Withdraw money from their bank account.
#3.check their account balance.
#4.quit the program.
print("enter your secret pin number to continue")
validid=445533
bank_balance=52300
while True:
    userid=int(input(":"))
    if validid!=userid:
       print("please enter a valid id")
       print("press q to exit ","press C to continue")
       enter=input("q or c")
       if enter=="c":
          print("continue")
       else:
          print("you have successfully exit")
          break
    else:
       print("you have the pin correctly you can continue")
       print("press q to exit ","press C to continue")
       enter=input("q or c: ")
       print()
       if enter=="q":
        print("you have successfully exit")
        break
       else:
         print("continue")
         print("Please select any of the options to continue")
         print("1.Money deposit" , "press 1")
         print("2.Money withdrawal" , "press 2")
         print("3.To Check Bank Balance " ,"press 3")
         list=[1,2,3]
         while True:
            option=int(input("please enter 1/2/3:--"))
            if option not in list:
               print("invalid input enter the again")
               continue
            else:
               if option==1:
                  print("you can deposit your amount")
                  deposit=int(input("enter your deposit amount"))
                  print("press q to exit ","press C to continue")
                  enter=input("q or c")
                  if enter=="q":
                    break
                  else:
                    print("continue")
                    total_balance= bank_balance + deposit
                    print("you have successfully deposited your amount")
                    print("your current balance is:= ",total_balance)
                    break
               elif option==2:
                  print("you can withdraw")
                  print("press C to continue","press q to exit ")
                  enter=input("q or c")
                  if enter=="q":
                    break
                  else:
                    print("continue")
                    withdrawal=int(input("please enter the amount you want to withdraw"))
                    if withdrawal>bank_balance:
                       print("insufficient balance")
                       print("your balance is",bank_balance)
                       break
                    else:
                      total_balance=bank_balance-withdrawal
                      print("you have successfull withdrawed",withdrawal)
                      print("And your current balance is=",total_balance)
                      break
               else:
                  print("your account Balance is=",bank_balance)
                  break
    break