"""
This program maintains a travel log of countries visited, the number of times each country was visited, 
and the cities visited within those countries. It allows the user to add new countries to the travel log 
and displays the most recently added country's information.

Done by Adeeb Imam
Date 31st May 2024
"""

def add_new_country(country, visits, list_of_cities):
    """
    Adds a new country to the travel_log.
    
    Parameters:
    country (str): The name of the country.
    visits (int): The number of times visited.
    list_of_cities (list): The list of cities visited in the country.
    """
    new_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    travel_log.append(new_country)

# Existing travel log
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Prompt user for input
country = input("Enter the country name: ")  # Add country name
visits = int(input("Enter the number of visits: "))  # Number of visits
# Input cities as a comma-separated string and split into a list
list_of_cities = input("Enter the cities visited, separated by commas: ").split(',')

# Add new country to the travel log
add_new_country(country, visits, list_of_cities)

# Print the newly added country information
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favorite city was {travel_log[2]['cities'][0].strip()}.")
