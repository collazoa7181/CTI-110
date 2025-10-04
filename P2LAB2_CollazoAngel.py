#Angel Collazo

#October 3,2025

#P2LAB2

#This program allows the user to select a vehicle from the dictionary, enter the miles that the user will drive and calculate gallon of gas needed.




vehicles = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
keys = vehicles.keys()

print(keys, "\n")

user_option = input("Enter a vehicle to see it's mpg: ")
mpg = vehicles[user_option]

print()# blank line

print(f"The {user_option} gets {vehicles[user_option]} mpg.\n")

miles = float(input(f"How many miles will you drive the {user_option}? "))
gallons_needed = miles / mpg

print()#blank line

print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {user_option} {miles:.1f} miles.\n")

              

    
