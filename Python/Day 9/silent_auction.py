"""
This program uses the knowledge of the lists and dictionary and with the help of it we 
are going to make a silent auction program

Done by Adeeb Imam
Date 31st May 2024
"""
import os

def clear_screen():
    # Clears the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def new_bidder(name, bid):
    new_bidders = {"name":name, "bid":bid,}
    auction.append(new_bidders)

def display_auction_banner():
    print("""
    ___________________
   |  _______________  |
   | |               | |
   | |  SILENT       | |
   | |  AUCTION      | |
   | |_______________| |
   |___________________|
         ||     ||
         ||     ||
         ||     ||
         ||_____||
        /_________\\
    """)

auction = []

# Display the auction banner
display_auction_banner()
print("Welcome to the silent auction!")

running = True

while running:

    name = input("Please enter your name: ")
    bid = int(input("Please input your bid: $ "))

    new_bidder(name,bid)

    next_person = input("are there any other people for the bid? (Yes or No): ").lower()
    if next_person == "yes":
        clear_screen()
    else:
        selling_price = 0

        for bid in auction:
            if bid["bid"] > selling_price:
                buyer_name = bid["name"]
                buying_price = bid["bid"]

        print(f"The highest bid was made by {buyer_name}, and the item is sold for ${buying_price}!")
        running = False

