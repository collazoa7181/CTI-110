#Angel Collazo
#October 8, 2025
#P2HW1
#This program calculates travel expenses


print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
print()#BLANK LINE
destination = input("Enter your travel destination: ")
print()#blank line
gas = float(input("How much do you think you will spent on gas? "))
print()#blank line
accommodation = float(input("Appoximately, how much will you need for accommodation/hotel? "))
print()#blank line
food = float(input("Last, how much do you need for food? "))



total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses
            
                     

print("\n------------Travel Expenses------------")
print(f"{"location: ":20}{destination}")
print(f"{"Initial Budget: ":20}${budget: ,.2f}")
print(f"{"Fuel: ":20}${gas: ,.2f}")
print(f"{"Accommodation: ":20}${accommodation: ,.2f}")
print(f"{"Food: ":20}${food: ,.2f}")
print("---------------------------------------\n")
print(f"{"Remaining Balance: ":20}${remaining_balance: ,.2f}")
      
