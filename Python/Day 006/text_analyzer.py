"""
In this function we take a string of text and return the word count, upper-case text and lower-case text
in the string

Done By Adeeb Imam
Date 23rd May 2024
"""

def text_len(text):
    text_len = len(text)
    return text_len

def upper_lower_count(text):
    upper_count = 0
    lower_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count



#Greeting the user at the start of the program

print("\nWelcome to the text analyzer")

running = True

while running:
    text = input("\nEnter the text that you want to anaylze, to end the program just click space: ")
    
    if text == " ":
        break
    else: 
        upper_count, lower_count = upper_lower_count(text)
        text_count = text_len(text)

        print(f"\nYour text has {text_count} characters with {upper_count} upper-case and {lower_count} lower-case")