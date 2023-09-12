# Create a Python module named "menu" that contains a dictionary representing the restaurant's menu items as keys
# and their prices as values. Write functions to add new items to the menu, remove items, and retrieve the price
# of a specific item.
# Import this module and use it to display the menu and calculate the total cost of a customer's order?
menuu={"Fry rice":150,"biriyani":200,"alfam":170,"shawarma":100}
def add():
    manager=input("items to add enter add""items to remove enter remove ""retrive the price of specific item enter retrive")
    if manager=="add":
        manage=input("enter the items the add")
        if manager not in menuu:
              price=int(input("enter the price of the item"))
              dict[manage]=price
    elif manager=="remove":
        remove=input("enter the items to remove")
        if remove in list:
            menuu.pop(remove)
    elif manager=="retrive":
        retrive=input("enter the item name to get the actual price")
        print(menuu[retrive])
def cost():
    print(menuu)
    x=0
    while x>len(menuu):
        purchase=input("enter the item")
        if purchase in menuu:
            sum=menuu[purchase]
            sum+=0
        x+=1
cost()
add()