"""
We are now learning the concept of randomisation 

This program generates a random number between a range of numbers given.

Done By Adeeb Imam
Date 19th May 2024
"""

import random #importing random to the functionaliltiy of randomisation

random_int = random.randint(1,10) #initilising a variable that would hold the value of the random number

print(f"Look every time you run the program you would get a random int (between 1 and 10): {random_int}")

random_float = random.random() #This random.random() produces a random floating number from 0 upto 1 (exclusive)
print(f"A random floating number between 0 and 1: {random_float} ")

"""
To expand the range of number from 0 to 1 (exclusive), we just need to multiply the random floating number
with the desired number end, example below demonstrates it well
"""

random_float = random_float*5 #keeping 5 (exclusive) as the limit we will get random number between 0 and 5 now

print(f"See now we are getting random numbers between 0 to 5: {random_float}")