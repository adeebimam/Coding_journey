"""
This program calculates the sum of all the even numbers given in a range of numbers

Done By Adeeb Imam
Date 22nd May 2024
"""

target = int(input("Please enter the end number till where you want to add the numbers (for e.g if you want to add from 1 to 100 just enter 100): "))

sum = 0

if target > 1000:
    print("Warning! the end number should be less than 1000")
else:
    for num in range(1, target+1):
        if num%2 == 0:
            sum += num
    print(f"The sum of even number from 1 to {target} is {sum}")