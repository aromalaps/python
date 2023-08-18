list=["pen","pencil","book","ink"]
i=0
lis=[]
while True:
    n=input(":")
    print("enter q to exit")
    if n=="q":
        break
    else:
       if n in list:
          if n not in lis:
             lis.append(n)
             print("you have purchased",n)
             if len(lis)==4:
                print("you have purchased maximum number of items in the list")
                break
             continue
       elif n not in list:
          print("invalid entry")
          print("please enter items existing in the list")
          continue