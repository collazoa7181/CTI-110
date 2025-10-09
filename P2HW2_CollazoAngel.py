#ANgel Collazo

#October 9, 2025

#P2HW2

#This program is designed to ask the user to enter grades for following tests. Each grade is to be requested in a separate statement.

#Github Link: 




#Program list

mod_grades =[]

# Module inputs

mod_1 = float(input("Enter grade for Module 1: "))
mod_grades.append(mod_1)
mod_2 = float(input("Enter grade for Module 2: "))
mod_grades.append(mod_2)
mod_3 = float(input("Enter grade for module 3: "))
mod_grades.append(mod_3)
mod_4 = float(input("Enter grade for Module 4: "))
mod_grades.append(mod_4)
mod_5 = float(input("Enter grade for Module 5: "))
mod_grades.append(mod_5)
mod_6 = float(input("Enter grade for Module 6: "))
mod_grades.append(mod_6)

#Calculation
                       
low_grade = min(mod_grades)
high_grade = max(mod_grades)
sum_grades = sum(mod_grades)
avg_grade = sum_grades / len(mod_grades)

#Display Results

print("\n-------------Results------------")
print(f"Lowest Grade:        {low_grade}")
print(f"Highest Grade:       {high_grade}")
print(f"Sum of grades:       {sum_grades}")
print(f"Average:             {avg_grade:.2f}")
print("----------------------------------------")




#Pseudocode
#The user will enter their grades score in each module input
#The program will stored all grades score input by the user separately inside the list
#The program will calculate the minimum, maximum, total and average grade scores
#The program will Display the results for the user
      
      
