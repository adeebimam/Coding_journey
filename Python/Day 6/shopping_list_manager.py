"""
This program is a shopping list manager where the user
can edit and see their shopping list

Done By Adeeb Imam
Date 23rd May 2024
"""

#Prompt the greeting for the user
print("Welcome to our shopping list")

engage = True
items = []  # Initialize an empty list to store shopping items

while engage:
    option = input("Please enter if you would like to edit, see your shopping list or exit: ").lower()

    if option not in ("see", "edit", "exit"):  # Check if the option is not in the list of valid options
        print("You have entered an invalid option. Please try again.")

    if option == "edit":
        add_or_edit_items = input("Would you like to add or remove items in your list? ").lower()

        if add_or_edit_items == "add":
            add_items = input("Please enter the items you wish to add to the list: ")
            items.append(add_items)  # Adds new item to the list
            
        elif add_or_edit_items == "remove":
            remove_items = input("Please enter the item you wish to remove from the list: ")
            if remove_items in items:
                items.remove(remove_items)  # Removes item from the list
            else:
                print("Item not found in the list.")

    elif option == "see":
        if items:  # Check if there are items in the list
            print(", ".join(items))  # Displays items separated by a comma and space
        else:
            print("Your shopping list is empty.")

    elif option == "exit":
        break
