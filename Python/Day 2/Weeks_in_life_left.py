"""
This program calculates the number of weeks left in someone's life
assuming the maximum life to be lived is 90 years. The input is taken
in years, and then the output is given in weeks.

Done by Adeeb Imam
"""

# Greeting the user for this program
print("Greetings! Welcome to the life calculator.")

# Assigning the constant for the age (number of weeks in 90 years)
max_weeks = 90 * 52.1429  # One year has approximately 52.1429 weeks

# Asking the user to input their age in years
current_age_years = float(input("Please enter your age in years: "))

# Converting the user's age into weeks
current_age_weeks = current_age_years * 52.1429

# Calculating the remaining weeks
weeks_remaining = max_weeks - current_age_weeks

# Outputting the age remaining, rounded to the nearest whole number
print(f"The age remaining is {round(weeks_remaining)} weeks.")
