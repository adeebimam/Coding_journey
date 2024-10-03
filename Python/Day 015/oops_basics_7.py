"""
In this program I am making the coffee machine again but this time with OOPS model

Done By Adeeb Imam (2nd October 2024)
"""

class CoffeeMachine:
    def __init__(self, water, milk, coffee, ):

        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.total_income = 0

    def report(self):
        return f"Generating the report\nThis coffee machine has {self.water}ml, {self.milk}ml and {self.coffee}g\n"

    def make_coffee(self,coffee_type):
        if coffee_type == "espresso":
            required_water = 30
            required_coffee = 9
            cost = 2.50
        elif coffee_type == "latte":
            required_water = 30
            required_milk = 300
            required_coffee = 9
            cost = 3.50
        elif coffee_type == "cappuccino":
            required_water = 30
            required_milk = 120
            required_coffee = 9
            cost = 3.00
        elif coffee_type == "end":
            return"ending the coffee machine"
        
        else:
            return "Invalid coffee type."
        
        if (coffee_type == "latte" or coffee_type == "cappuccino") and (required_milk > self.milk):
            return f"Sorry we have less milk and cannot make your {coffee_type}"
        if required_coffee > self.coffee:
            return f"Sorry we have less coffee and cannot make your {coffee_type}"
        if required_water > self.water:
            return f"Sorry we do not have enough water and cannot make your {coffee_type}"
        # Deduct the ingredients
        self.water -= required_water
        self.coffee -= required_coffee
        if coffee_type == "latte" or coffee_type == "cappuccino":
            self.milk -= required_milk

        return cost
    
    def make_transaction(self,cost):
        print(f"Please pay {cost}")
        

        
       
morning_machine = CoffeeMachine(1000,300,200)

running = True

while running == True:

    
    user_coffee = input("Please input the coffee needed: ").lower()
    if user_coffee == "end":
        result = morning_machine.make_coffee(user_coffee)
        print(result)
        running = False
    elif(user_coffee == "report"):
        print(morning_machine.report())
    else:
        result = morning_machine.make_coffee(user_coffee)
        print(result)
    




