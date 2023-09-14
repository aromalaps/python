# Create a Python module named "menu" that contains a dictionary representing the restaurant's menu items as keys
# and their prices as values. Write functions to add new items to the menu, remove items, and retrieve the price
# of a specific item.
# Import this module and use it to display the menu and calculate the total cost of a customer's order?
menuu={"Fry rice":150,"biriyani":200,"alfam":170,"shawarma":100}
def add():
    manager=input("items to add enter add""items to remove enter remove ""retrive the price of specific item enter retrive or enter purchase to calculate ")
    if manager=="add":
        manage=input("enter the items the add")
        if manager not in menuu:
              price=int(input("enter the price of the item"))
              menuu[manage]=price
    elif manager=="remove":
        remove=input("enter the items to remove")
        if remove in list:
            menuu.pop(remove)
    elif manager=="retrive":
        retrive=input("enter the item name to get the actual price")
        print(menuu[retrive])
    elif manager=="purchase":
        print("enter the items to calculate")
    
    else:
        print("invalid entry")
        add()
def cost():
    print(menuu)
    x=0
    sum=0
    while x<len(menuu):
        purchase=input("enter the item")
        if purchase in menuu:
            count=int(input("enter the count"))
            sum+=menuu[purchase]
            sum*=count
        elif purchase=="exit":
            break
        else:
            print("this item is not in the list",menuu)
        x+=1
    print(sum)
