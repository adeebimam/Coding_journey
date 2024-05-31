"""
In this program we would use the Caesar Cipher technique to 
encrypt and decrypt our message

Done By Adeeb Imam
Date 28th May 2024
"""

def caesar(text, shift, cryptograph):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cryptograph == "encrypt":
                new_position = position + shift
            else: 
                new_position = position - shift
            new_letter = alphabet[new_position % len(alphabet)]
            cipher_text += new_letter
        else:
            cipher_text += letter
    
    if cryptograph == "encrypt":
        print(f"The encryption for {text} is '{cipher_text}'")
    else: 
        print(f"The decryption for {text} is '{cipher_text}'")


alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z']

running = True

while running:
    print("\n")
    direction = input("Type 'encrypt' to encrypt the data or 'decrypt' to decrypt the data: ").lower()
    text = input("Please enter your message here: ")
    text = text.lower()
    shift = int(input("Type the shift number: "))

    shift = shift % 26

    caesar(text, shift, direction)
    print("\n")

    update_running = input("Would you like to run the program again? (yes/no): ").lower()
    
    if update_running != "yes":
        running = False
