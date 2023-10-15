# Create a Python script to check the password strength. 

# Implement a Python function called check_password_strength that takes a password string as input.

# importing regular regular expressions
import re
# create a variable that can store the input string which will provided by user
password = str(input("Please enter a password: "))

def check_password_strength(password1):

    # Check if the password has at least 8 characters
    if len(password1) < 8:
        return "Entered password does not meet the length criteria: Minimum 8 characters"
    # Check if the password contains at least one uppaercase letter
    elif not re.search(r'[A-Z]',password1):
        return "Enterd password does not contain an uppercase letter."
    # Check if the password contains at least one lowercase letter
    elif not re.search(r'[a-z]',password1):
        return "Entered password does not contain a lowercase letter."
    # Check if the password contains at least one digit
    elif not re.search(r'[1234567890]',password1):
        return "Entered password does not contain a digit."
    # Check if the password contains at least one special charcater
    elif not re.search(r'[!@#$%^&*()]',password1):
        return "Enterd password does not contain a special charcater: allowed characters - !@#$%^&*()"
    else:
        return "Password has met the password policy criteria."
    
print(check_password_strength(password))