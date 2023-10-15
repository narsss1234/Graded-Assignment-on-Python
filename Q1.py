# Create a Python script to check the password strength. 

# Implement a Python function called check_password_strength that takes a password string as input.

# importing regular regular expressions
import re


def check_password_strength(password1):

    # Check if the password has at least 8 characters
    if len(password1) < 8:
        return False
    # Check if the password contains at least one uppaercase letter
    elif not re.search(r'[A-Z]',password1):
        return False
    # Check if the password contains at least one lowercase letter
    elif not re.search(r'[a-z]',password1):
        return False
    # Check if the password contains at least one digit
    elif not re.search(r'[1234567890]',password1):
        return False
    # Check if the password contains at least one special charcater
    elif not re.search(r'[!@#$%^&*()]',password1):
        return False
    else:
        return True
    
# create a variable that can store the input string which will provided by user
password = str(input("Please enter a password: "))

if check_password_strength(password):
    print("The entered password meets the password policy criteria.")
else:
    print("The password does not meet the criteria:\n")
    print("○ Minimum length: The password should be at least 8 characters long.\n")
    print("○ Contains both uppercase and lowercase letters.\n")
    print("○ Contains at least one digit 0-9.\n")
    print("○ Contains at least one special character !@#$%^&*()\n")