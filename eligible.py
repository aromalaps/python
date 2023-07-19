print("valid the eligibility")
math=int(input("enter a value"))
phy=int(input("enter a value"))
chem=int(input("enter a value"))
total=math+phy+chem
if total>190:
 print("you are eligible")
elif phy+chem>140:
 print("you are eligible")
else:
  print("you are not eligible")