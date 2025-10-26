#Angel Collazo

#October 26, 2025

#P3HW2

#This program will ask the user to input their name, hours worked and pay rate.
#Then the program will calculate and display the user's hours worked, pay rate, overtime hours,
#overtime pay, regular hours pay and the total pay.

#Github Link:



# User will input the information the program is asking

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Program Calculation

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

#Program Display

print("-------------------------------------")
print(f"{'Employee Name:':<20}{employee_name}\n")
print("Hours Worked   Pay Rate    OverTime    OverTime Pay        RegHour Pay         Gross Pay")
print("----------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<20.2f}${regular_pay:<19.2f}${gross_pay:.2f}")




#Pseudocode:
#The program will ask the user to input their name
#The program will ask the user to input the worked hours
#The program will ask the user to input their pay rate
#the program then calculate the overtime hours, overtime pay, regular pay and gross pay
#The program will display all results
