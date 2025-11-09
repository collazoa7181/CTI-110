# Angel Collazo

# November 7, 2025

# P4HW2

# This program calculates gross pay for multiple employees, including overtime pay,
# and displays totals for all employees entered.


total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

#The program ask for first employee name
employee_name = input("Enter employee's name or 'Done' to terminate: ")

while employee_name != "Done":
#Inputs
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))


    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    
 
    print(f"\nEmployee name: {employee_name}")

    print("\nHours Worked   Pay Rate    OverTime    OverTime Pay      RegHour Pay         Gross Pay")
    print("--------------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<18.2f}${regular_pay:<19.2f}${gross_pay:.2f}\n")
   
    

    
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

#The program will ask for next employee
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

#Display

print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

#Pseudocode
#The program will asks the user employee name
#The user will enter user pay rate and hours worked
#The program will calculate overpay and regular pay.
#The program will store these values in variables.
#The program will display overtime total, regular pay total, gross pay total, and number of employees entered
#The program will ask the user to enter another employee's name to calculate salary for or "Done" to terminate program.

