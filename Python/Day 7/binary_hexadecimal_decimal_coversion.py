"""
This program converts between binary, hexadecimal, and decimal
by using user input to know the value and what conversion to do.

Done By Adeeb Imam
Date 25/05/2024
"""

def bin_to_dec(num):
    return int(num, 2)

def deci_to_bin(num):
    return bin(int(num))[2:]

def hexa_to_deci(num):
    return int(num, 16)

def deci_to_hexa(num):
    return hex(int(num))[2:]

def bin_to_hexa(num):
    deci_num = bin_to_dec(num)
    return deci_to_hexa(deci_num)

def hexa_to_bin(num):
    deci_num = hexa_to_deci(num)
    return deci_to_bin(deci_num)


# Prompt a greeting to the user at the start of the program
print("Welcome to the number systems converter")

running = True

while running:
    conversion = input("What kind of conversion would you like to do: ")
    conversion = conversion.lower()
    possible_conversion = ["binary to decimal", "bin to deci", "binary to hexadecimal", "bin to hexa",
                           "decimal to binary", "deci to bin", "decimal to hexadecimal", "deci to hexa",
                           "hexadecimal to binary", "hexa to bin", "hexadecimal to decimal", "hexa to deci"]

    if conversion not in possible_conversion:
        print("The number system conversion is not valid!")
    else:
            if conversion in ("binary to decimal", "bin to deci"):
                num = input("Please enter the number that you would like to convert from BINARY to DECIMAL: ")
                ans = bin_to_dec(num)
                print(f"Converting {num} from BINARY to DECIMAL: {ans}")

            elif conversion in ("binary to hexadecimal", "bin to hexa"):
                num = input("Please enter the number that you would like to convert from BINARY to HEXADECIMAL: ")
                ans = bin_to_hexa(num)
                print(f"Converting {num} from BINARY to HEXADECIMAL: {ans}")

            elif conversion in ("decimal to binary", "deci to bin"):
                num = input("Please enter the number that you would like to convert from DECIMAL to BINARY: ")
                ans = deci_to_bin(num)
                print(f"Converting {num} from DECIMAL to BINARY: {ans}")

            elif conversion in ("decimal to hexadecimal", "deci to hexa"):
                num = input("Please enter the number that you would like to convert from DECIMAL to HEXADECIMAL: ")
                ans = deci_to_hexa(num)
                print(f"Converting {num} from DECIMAL to HEXADECIMAL: {ans}")

            elif conversion in ("hexadecimal to binary", "hexa to bin"):
                num = input("Please enter the number that you would like to convert from HEXADECIMAL to BINARY: ")
                ans = hexa_to_bin(num)
                print(f"Converting {num} from HEXADECIMAL to BINARY: {ans}")

            elif conversion in ("hexadecimal to decimal", "hexa to deci"):
                num = input("Please enter the number that you would like to convert from HEXADECIMAL to DECIMAL: ")
                ans = hexa_to_deci(num)
                print(f"Converting {num} from HEXADECIMAL to DECIMAL: {ans}")
                

