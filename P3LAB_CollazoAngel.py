 #Angel Collazo

 #October 17, 2025

 #P3LAB1

 #This program allows the user to enter a money (float) value and the program should then calculate the most

 #efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money

 #Github Link: 




#Get the value from the User
change = float(input("Enter the amount of money as a float: $"))


#Converting the value to an integer
change = round(change * 100)


#Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quaters = change // 25
change = change - (num_quaters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change


if num_dollars > 0:
    if num_dollars ==1:
        print(f"{num_dollars} Dollar")
    else:
       print(f"{num_dollars} Dollars")

if num_quaters > 0:
    if num_quaters ==1:
        print(f"{num_quaters} Quater")
    else:
       print(f"{num_quaters} Quaters")

if num_dimes > 0:
    if num_dimes ==1:
        print(f"{num_dimes} Dime")
    else:
       print(f"{num_dimes} Dimes")

if num_nickels > 0:
    if num_nickels ==1:
        print(f"{num_nickels} Nickel")
    else:
       print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies ==1:
        print(f"{num_pennies} Penny")
    else:
       print(f"{num_pennies} Pennies")

if change == 0:
    print(f" YOU ARE BROKE!")





