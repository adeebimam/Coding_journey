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

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("Please enter the first digit: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Please pick one of the operations from the line above: ")

num2 = int(input("Please enter the second digit: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

running = True

while running:
    ask_running = input("Do you want to continue the calculation? (Y/N): ").lower()

    if ask_running == 'y':
        num = int(input(f"Please enter the digit that would operate with {answer}: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Please pick one of the operations from the line above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(answer, num)
        print(f"{answer} {operation_symbol} {num} = {answer}")
    elif ask_running == 'n':
        running = False
        print("The program has ended thank you!")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

