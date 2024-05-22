"""
In this program we look at a new concept known as loops more specifically "for loops"

For loops iterate over sequences (lists, strings, etc.) or a range of numbers, 
executing a block of code for each item.

Done By Adeeb Imam
Date 22nd May 2024
"""

# Prompt the user for input and split it into a list of strings
student_heights = input("Please enter student heights separated by space: ").split()

# Convert each string in the list to an integer
student_heights = [int(height) for height in student_heights]

# Initialize the total_height variable
total_height = 0

# Iterate over each height in the student_heights list
for height in student_heights:
    total_height += height  # Add each height to the total_height
    avg_height = total_height/len(student_heights)

# Print the total_height
print(f"The heights that you have entered are {student_heights}\nThe average height is {avg_height}")

