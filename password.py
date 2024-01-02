# Import the random module for generating random characters
import random

# Define character sets for different types of characters

# Uppercase letters
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Lowercase letters
lowercase_letters="abcdefghijklmnopqrstuvwxyz"

# Digits
digits='1234567890'

# Special characters
special_char="!@$%&*_-+=?><~`"


upper = True   # Include uppercase letters
lower = True   # Include lowercase letters
nums = True    # Include digits
syms = True    # Include special characters


# Create the combined character pool based on requirements
all=""

if upper:
    all += uppercase_letters
    
if lower:
    all += lowercase_letters 
    
if nums:
    all += digits
    
if syms:
    all += special_char       
        
    
# Get user input for password length and quantity
length = int(input("Enter desired password length: "))
amount = int(input("Enter how many passwords to generate: "))  


# Generate and print the specified number of passwords
for x in range(amount):
    password="".join(random.sample(all, length))
    print("your random password is :", password)