"""
In this program we calculate how much cans of paint we would
require to paint a wall, given that the height and width is user input

Done By Adeeb Imam
Date 28th May 2024
"""
import math

def paint_area(height,width):
    coverage = 5
    num_of_cans = (height*width)/coverage
    return math.ceil(num_of_cans)

print("Greeting welcome to the paint_required_program !")

height = int(input("Please input the height of the wall: "))
width = int(input("Please input the width of the wall: "))

required_cans = paint_area(height,width)

print(f"You would require {required_cans} of cans to paint your wall")

