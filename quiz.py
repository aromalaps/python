#quiz
"""print("we have conducted a quiz")
print("In our quiz have 5 questions and each correct answer gives 5 points and each wrong answer will your 2 points will drain")
y=input("enter yer or no to continue")"""
print("what is the sum of 5+6")
print("options:")
print("a=10")
print("b=11")
print("c=13")
print("d=9")
answer="b"
sum=input("please select the option")
if answer==sum:
    print("your answer is correct")
    scored=5
    print("you have scored 5 points",scored)
elif answer != sum:
    print("your answer is wrong")
    scored=-2
    print("your score is",scored)
print("succesfully you can continue to the second question")
print("what is the sum of 100-50")
print("options:")
print("a=60")
print("b=70")
print("c=50")
print("d=-50")
answer="c"
sum=input("please select the option")
if answer==sum:
    print("your answer is correct")
    print("you have scored 5 points")
    scored2=scored+5
    print("your score is",scored2)
elif answer != sum:
    print("your answer is wrong")
    scored2=scored-2
    print("your score is",scored2)
print("succesfully you can continue to the third question")
print("what is the sum of 100*2")
print("options:")
print("a=200")
print("b=120")
print("c=2000")
print("d=1200")
answer="a"
sum=input("please select the option")
if answer==sum:
    print("your answer is correct")
    print("you have scored 5 points")
    scored3=scored2+5
    print("your score is",scored3)
elif answer != sum:
    print("your answer is wrong")
    scored3=scored2-2
    print("your score is",scored3)
    total=scored3
    print("your total score =",total)