"""
In this program we are checking if a number is prime or not
the range of the number is 1 to 100

Done By Adeeb Imam
Date 28th May 2024
"""
import math
max_num = 100
is_prime = True

num_check = input("Please enter the number that you want to check if it is prime or not (Range is 1 to 100): ")
num_check = int(num_check)

if num_check > 100 or num_check < 1:
    print("The number is not in the range! ")
else: 
    if num_check < 2:
        print("Not a prime number")
    elif num_check == 2:
        print("It is a prime number")
    elif num_check > 2 and (num_check % 2 == 0 or any(num_check % i == 0 for i in range(3, int(math.sqrt(num_check)) + 1, 2))):
        print("It is not a prime number")
    else:
        print("It is a prime number")


    