#Done by Adeeb Imam on 11th May 2024

#The project for day 1 is to create a band name generator, 
#where the name of the band is generated on the follwing 
#things name of the city, name of a pet and then combine 
#the name of the pet and city

#1. Creating a greeting for the program
print("Hello welcome to the Band name generator")

#2. Ask the user to enter the city name they grew up in
city_name = input("Please enter the city you grew up in: ")

#3. Ask the user to enter the name of a pet.
pet_name = input("Please enter the name of a pet: ")

#4. Combine the name of the city and the pet
band_name = city_name + " " + pet_name

#5. Print the name of the band
print(f"The name of the band is '{band_name}'")