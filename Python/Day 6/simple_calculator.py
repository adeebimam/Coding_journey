"""
In this project we would learn a new concept known as "Functions"

Functions are reusable blocks of code that perform specific tasks and can optionally return values.

This program is a simple calculator that has the functionality to ADD, SUBTRACT, MULTIPLY, AND DIVIDE
and the operation is between 2 digits only

Done By Adeeb Imam
Date 23rd May 2024
"""

def add(digit1, digit2):
    return digit1+digit2

def subtract(digit1, digit2):
    return digit1-digit2

def multiply(digit1, digit2):
    return digit1*digit2

def divide(digit1, digit2):
    if digit2 == 0:
        print("The denominator cannot be a 0!")
    else:
        return digit1/digit2




#Greeting the user at the start of the program
print("Welcome to your favourite calculator!")

running = True

while running:
    operation = input("\nPlease input if you would like to ADD, SUBTRACT, MULTIPLY or DIVIDE (You can also use signs). To end the program simply type end: ")
    operation = operation.lower()

    print("\n")

    if operation in ("add" , "+"):

        digit1 = float(input("Please enter the first digit you would like to ADD: "))
        digit2 = float(input("Please enter the second digit you would like to ADD: "))
        
        result = add(digit1, digit2)
        print(f"\nThe result of your arthematic calculation is {result:.2f}")

    if operation in ("subtract" , "-"):
        digit1 = float(input("Please enter the first digit you would like to SUBTRACT: "))
        digit2 = float(input("Please enter the second digit you would like to SUBTRACT: "))

        result = subtract(digit1, digit2)
        print(f"\nThe result of your arthematic calculation is {result:.2f}")

    if operation in ("multiply" , "*"):
        digit1 = float(input("Please enter the first digit you would like to MULTIPLY: "))
        digit2 = float(input("Please enter the second digit you would like to MULTIPLY: "))

        result = multiply(digit1, digit2)
        print(f"\nThe result of your arthematic calculation is {result:.2f}")


    if operation in ("divide" , "/"):
        digit1 = float(input("Please enter the first digit you would like to DIVIDE: "))
        digit2 = float(input("Please enter the second digit you would like to DIVIDE: "))

        result = divide(digit1, digit2)
        print(f"\nThe result of your arthematic calculation is {result:.2f}")
    
    if operation == "end":
        break


    

