user=int(input("enter a value"))
def factorial(use):
    if use==0 or use==1:
        return 1
    else:
        return use * factorial(use-1)
s=factorial(user)
print(s)