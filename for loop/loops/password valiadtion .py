#write a python program that takes a string input from the user and validate it using a for loop.
#the password must meet the following conditions:
#(i) it should be at least  8 characters long.
#(ii) it should contain at least one uppercase letter.
#(iii) it should contain atleast one lowercase letter.
#(iv) it should contain at least one digit.
password = "SecurePass123"
for i in password:
    if i.isupper():
        print("Password is valid.")
    else:
        print("Password must contain at least one uppercase letter.")