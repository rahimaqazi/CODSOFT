# This program performs basic arithmetic operations on two numbers based on user input.


# Get input for the two numbers
Num1 = int(input("Enter a 1st Number : "))  # Store the first number as an integer
Num2 = int(input("Enter a 2nd Number : "))  # Store the second number as an integer


# Display a menu of arithmetic operations

print("1. Addition")  # Option 1 for addition
print("2. Subtraction")  # Option 2 for subtraction
print("3. Division")  # Option 3 for division
print("4. Multiplication")  # Option 4 for multiplication

# Get user's choice of operation
choice = int(input("Enter Your Choice 1-4 :"))  # Store the user's choice as an integer


# Perform the chosen operation
if choice == 1:
   sum = Num1 + Num2  # Calculate the sum
   print(f"Addition of Two Numbers = {sum}")  # Print the result

elif choice == 2:
   sub = Num1 - Num2  # Calculate the difference
   print(f"Subtraction of Two Numbers = {sub}")  # Print the result

elif choice == 3:
   div = Num1 / Num2  # Calculate the quotient (division)
   print(f"Division of Two Numbers = {div}")  # Print the result

elif choice == 4:
   mul = Num1 * Num2  # Calculate the product (multiplication)
   print(f"Multiplication of Two Numbers = {mul}")  # Print the result

else:
   print("Invalid Choice")  # Notify the user if they entered an invalid choice
