"""
This program takes any number and checks if it is odd or even.

Done By Adeeb Imam on 19th May 2024
"""

# Greeting the user at the start of the program
print("Greetings! Welcome to the number checker program.")

# Ask the user to enter a number
num = input("Please enter the number that you want to check is odd or even: ")

# Convert the input to an integer
num_int = int(num)

# Check if the number is odd or even
if num_int % 2 == 0:
    print(f"The number entered {num} is even.")
else:
    print(f"The number entered {num} is odd.")
