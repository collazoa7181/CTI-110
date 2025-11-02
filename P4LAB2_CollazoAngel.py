#Angel Collazo
#Nobember 2, 2025
#P4LAB2_AngelCollazo
#Use while loop and for loop together

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if the number is negative, tell user that the program cannot accept it
Ask user to run the program
if yes, run the program
if no, end the program
'''
run_again = "yes"

while run_again != "no":
            
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #Display multiplication for that value and range (1-12)       
        for item in range(1, 13):   
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")

    run_again = input("Would you like to run the program again? ")

#Loop has brocken. User entered "no"
print("Program is ending...")

        
        




