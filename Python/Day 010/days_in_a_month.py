"""
In this program we would be taking our pre-existing knowledge about functions and enhance it to
make a better program in counting days in a month.

Done By Adeeb Imam
Date 31st  May 2024
"""

def is_leap_year(year):
    if year % 400 == 0:
        return True
    
    elif year % 100 == 0:
        return False
    
    elif year % 4 == 0:
        return True
    
    else:
        return False


def days_in_a_month(year,month):
    
    if month in (1,3,5,7,8,10,12):
         days =31
    elif month == 2:

        if is_leap_year(year) == True:
            days = 29
        else:
            days = 28
    else:
        days = 30
    
    return days

print("Welcome to calendar-day checker!")
user_month = int(input("Please enter the month (in number): "))
user_year = int(input("Please enter the year: "))

days = days_in_a_month(user_year,user_month)

print(f"The month {user_month} has {days} in the year {user_year}")