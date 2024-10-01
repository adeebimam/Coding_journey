""""
This project simulates a coffee machine, where the user can choose between
a variety of coffee's. It also processes payments, update the resources and 
also provide a report

Done By Adeeb Imam
Date 9th June 2024
"""

water = 1000
milk = 500
coffee = 760

total_cost = 0
return_amount = 0

def get_positive_currency(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("\nPlease enter a positive number!\n")
            else:
                return value
        except ValueError:
            print("\nInvalid input, please enter a number.\n")
            


def report(water, milk, coffee):
    print(f"You have {water}ml water, {milk}ml milk, and {coffee}g coffee\n")


print("\nGreetings welcome to coffee machine")

running = True

while running:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    

    if coffee_choice == "off":
        running = False
    
    elif coffee_choice == "report":
        report(water, milk, coffee)
        

    elif coffee_choice == "cappuccino":
        if water >= 30 and coffee >= 9 and milk >= 120:
        
            water = water - 30
            coffee = coffee - 9 
            milk = milk - 120 
            total_cost = 3.00
        else:
            print("Insufficient ingredients for cappuccino. Try another option.")
            continue

    elif coffee_choice == "latte":
        if water >= 30 and coffee >= 9 and milk >= 300:
            water = water - 30 
            coffee = coffee - 9 
            milk = milk - 300 
            total_cost = 3.50
        else:
            print("Insufficient ingredients for latte. Try another option.")
            continue
        

    elif coffee_choice == "espresso":
        if water >= 30 and coffee >= 9:        
            water = water - 30 
            coffee = coffee - 9 
            total_cost = 2.50
        else:
            print("Insufficient ingredients for latte. Try another option.")
            continue


    else:
        print("Invalid input please try again")
        continue

    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        if water > 0 and coffee > 0 and milk > 0:
            print(f"we can make your {coffee_choice}, \nThe total cost of your {coffee_choice} is ${total_cost}")

            while True:

                quarters = get_positive_currency("\nPlease enter the quarters that you have (only numbers): ")
                quater_amount = quarters*0.25

                dimes = get_positive_currency("Please enter the dimes that you have (only numbers): ")
                dimes_amount = dimes*0.10

                nickles = get_positive_currency("Please enter the nickles that you have (only numbers): ")
                nickles_amount = nickles*0.05

                pennies = get_positive_currency("Please enter the pennies that you have (only numbers): ")
                pennies_amount = pennies*0.01

                total_amount_paid = quater_amount + dimes_amount + nickles_amount + pennies_amount

                if total_amount_paid >= total_cost:
                    if total_amount_paid > total_cost:
                        return_amount = total_amount_paid - total_cost
                        print(f"\nEnjoy is your {coffee_choice}!\nHere is a breakdown of your purchase\nItem:{coffee_choice}\nTotal cost: ${total_cost}\nAmount paid: ${total_amount_paid}\nChange: ${return_amount:.1f}\n")
                        break
                else:
                    print(f"Sorry the total cost of the drink was ${total_cost} and you have paid ${total_amount_paid:.1f}\n")
                    while True:
                        choice = input("Would you like to try again or cancel the program? ").lower()
                        if choice == "cancel":
                            running = False
                            break
                        elif choice == "try again":
                            print("Let us try again")
                            break
                        else:
                            print("Invalid choice please enter 'try again' or 'cancel'")
                if not running:
                    break 

                    

        
        else:
            print(f"We dont have sufficient stuff ingredients to make your drink, please try again later\n")
            
        
    






