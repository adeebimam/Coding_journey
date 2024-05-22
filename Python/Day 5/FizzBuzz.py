"""
This program prints the solution to the FizzBuzz game, the program prints numbers for 1 to 100 (including 100)
when the number is divisible by 3 then instead of printing the number it would print "Fizz"
when the number is divisible by 5 then instead of printing the number it would print "Buzz"
when the number is divisibel by both 5 and 3 then instead of printint the number it would print "FizzBuzz"

Done By Adeeb Imam
Date 22nd May 2024
"""

#Greeting the user at the start of the program
print("Welcome to the FizzBuzz game, let the fun begin!")

#Running the for loop from 1 to 100 int number
for num in range(1,101):

    x = num #assinging the number value to varibale x

#Using the if and else statment to check if the number is divisible by 3, 5 or both and then assigning the desired output
    if num % 3 == 0 and num % 5 == 0: 
        x = "FizzBuzz"

    elif num % 3 == 0:
        x = "Fizz"

    elif num % 5 == 0:
        x = "Buzz"

    print(x)
