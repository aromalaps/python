def factorial(a):
    fact=1
    for i in range(1,a):
       fact=i*a
    print(fact)
a=int(input("enter a number"))
factorial(a)