"""
This program performs basic arithmetic operations on user-inputted numbers,
allowing continuous calculations with the result until the user decides to stop.

Done By Adeeb Imam
Date 31st May 2024
"""

def add(digit1, digit2):
    return digit1 + digit2

def subtract(digit1, digit2):
    return digit1 - digit2

def multiply(digit1, digit2):
    return digit1 * digit2

def divide(digit1, digit2):
    if digit2 == 0:
        return "The denominator cannot be a 0!"
    else:
        return digit1 / digit2
def exponent(digit1, digit2):
    return digit1**digit2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "pow": exponent,
}

def perform_operation(num1, num2, operation_symbol):
    if operation_symbol in operations:
        calculation_function = operations[operation_symbol]
        return calculation_function(num1, num2)
    else:
        return "Invalid operation symbol!"

num1 = float(input("Please enter the first digit: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Please pick one of the operations from the line above: ")

num2 = float(input("Please enter the second digit: "))

answer = perform_operation(num1, num2, operation_symbol)
if isinstance(answer, str):
    print(answer)
else:
    print(f"{num1} {operation_symbol} {num2} = {answer}")

running = True

while running:
    ask_running = input("Do you want to continue the calculation? (Y/N): ").lower()

    if ask_running == 'y':
        num = float(input(f"Please enter the digit that would operate with {answer}: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Please pick one of the operations from the line above: ")
        new_answer = perform_operation(answer, num, operation_symbol)
        if isinstance(new_answer, str):
            print(new_answer)
        else:
            print(f"{answer} {operation_symbol} {num} = {new_answer}")
            answer = new_answer
    elif ask_running == 'n':
        running = False
        print("The program has ended. Thank you!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

