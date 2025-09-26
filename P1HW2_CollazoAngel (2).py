#Angel Collazo

#September 25,2025

#P1HW2

#The user has to input btheir travel budget

#Calculate expenses and display results



print("This program calculates and displays travel expenses","\n")

budget = int(input("Enter your budget: "))
print()#This line is a blank space
destination = input("Enter your travel destination: ")
print()#This line is a blank space
gas = int(input("How much will you spend for gas: "))
print()#This line is is a blank space
accomodation = int(input("How much will you spend on accomodation? "))
print()#This line is a blank space
food = int(input("How much will you spend on food? "))


#Calculate Total expenses and remaining budget


total_expenses = gas + accomodation + food
remaining_budget = budget - total_expenses

remaining_balance = budget - total_expenses

#Display results

print("\n------------Travel Summary------------")

print("Destination: ", destination)
print("Initial budget: ",budget,"\n")
print("Fuel: ",gas)
print("Accomodation: ",accomodation)
print("Food: ",food,"\n")


print("Remaining Balance: ",remaining_balance)

# Pseudocode:
# The user has to enter their total budget and store it
# The user has to enter travel destination and store it
# The user has to enter gas expense and store it
# The user has to enter accommodation expense and store it
# The user has to enter food expense and store it
# The program will calculate total expenses by adding gas, accommodation, and food
# The program will subtract total expenses from budget to get remaining balance
# The end result is that the program will display travel destination, initial budget, total expenses, and remaining balance


