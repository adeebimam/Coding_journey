"""
    This project takes the height and weight as the input
    from the user and tells where does their BMI lie on 
    the BMI index

    Done By Adeeb Imam on 19th May 2024
"""

#Greeting message for the BMI calculator
print("Welcome to BMI calculator")

#Ask the user to input their name
name = input("Please enter your name: ")

#Ask the user to input their height in centi-meters
height = float(input("Please enter your height in cm: "))

#Ask the user to input their weight in kilograms
weight = float(input("Please enter your weight in kg: "))

#Conversion and BMI calculation

height = height/100
sq_height = height**2

BMI = float(f"{weight/sq_height:.1f}")

#If else statment for the category of BMI

if BMI < 16:
    BMI_category = "Severe Thinness"
elif BMI >= 16 and BMI <= 17:
    BMI_category = "Moderate Thinness"
elif BMI >= 17 and BMI <= 18.5:
    BMI_category = "Mild Thinness"
elif BMI >= 18.5 and BMI <= 25:
    BMI_category = "Normal"
elif BMI >= 25 and BMI <= 30:
    BMI_category = "Overweight"
elif BMI >= 30 and BMI <= 35:
    BMI_category = "Obese Class 1"
elif BMI >= 35 and BMI <= 40:
    BMI_category = "Obese Class 2"
else:
    BMI_category = "Obese Class 3"

print(f"Dear {name}, \nYour BMI is {BMI} and you are in the {BMI_category} category")
