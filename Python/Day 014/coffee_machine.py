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


def report(water, milk, coffee):
    print(f"You have {water}ml water, {milk}ml milk, and {coffee}g coffee\n")


print("\nGreetings welcome to coffee machine")

running = True

while running:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print("\n")

    if coffee_choice == "off":
        running = False
    
    elif coffee_choice == "report":
        report(water, milk, coffee)
        

    elif coffee_choice == "cappuccino":
        water = water - 30
        coffee = coffee - 9 
        milk = milk - 120 
        total_cost = 3.00

    elif coffee_choice == "latte":
        water = water - 30 
        coffee = coffee - 9 
        milk = milk - 300 
        total_cost = 3.50

    
    elif coffee_choice == "espresso":
        water = water - 30 
        coffee = coffee - 9 
        total_cost = 2.50

    else:
        print("Invalid input please try again")

    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        if water > 0 and coffee > 0 and milk > 0:
            print(f"we can make your {coffee_choice}, \nThe total cost of your {coffee_choice} is ${total_cost}")

            quarters = float(input("Please enter the quarters that you have: "))
            quater_amount = quarters*0.25

            dimes = float(input("Please enter the dimes that you have: "))
            dimes_amount = dimes*0.10

            nickles = float(input("Please enter the nickles that you have: "))
            nickles_amount = nickles*0.05

            pennies = float(input("Please enter the pennies that you have: "))
            pennies_amount = pennies*0.01

            total_amount_paid = quater_amount + dimes_amount + nickles_amount + pennies_amount

            if total_amount_paid >= total_cost:
                if total_amount_paid > total_cost:
                    return_amount = total_amount_paid - total_cost
                    print(f"\nEnjoy is your {coffee_choice}!\nHere is a breakdown of your purchase\nItem:{coffee_choice}\nTotal cost: ${total_cost}\nAmount paid: ${total_amount_paid}\nChange: ${return_amount:.1f}\n")
            else:
                print(f"Sorry the total cost of the drink was ${total_cost} and you have paid ${total_amount_paid:.1f}\n")
                running = False

        
        else:
            print(f"We dont have sufficient stuff ingredients to make your drink, please try again later\n")
            running = False
        
    






