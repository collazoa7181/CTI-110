#Angel Collazo

#October 25, 2025

#P3HW1

#This program takes a number grade , determines average and displays letter grade for average.

#Github Link:

mod_grades =[]

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_grades.append(mod_1)
mod_2 = float(input('Enter grade for Module 2: '))
mod_grades.append(mod_2)
mod_3 = float(input('Enter grade for Module 3: '))
mod_grades.append(mod_3)
mod_4 = float(input('Enter grade for Module 4: '))
mod_grades.append(mod_4)
mod_5 = float(input('Enter grade for Module 5: '))
mod_grades.append(mod_5)
mod_6 = float(input('Enter grade for Module 6: '))
mod_grades.append(mod_6)

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low_grade = min(mod_grades)
high_grade = max(mod_grades)
sum_grades = sum(mod_grades)
avg_grade = sum_grades / len(mod_grades)

print("\n-------------Results------------")
print(f"Lowest Grade:        {low_grade}")
print(f"Highest Grade:       {high_grade}")
print(f"Sum of grades:       {sum_grades}")
print(f"Average:             {avg_grade:.2f}")
print("----------------------------------------")

# determine letter grade for average


if avg_grade >= 90:
    print('Your grade is: A')

elif avg_grade >= 80:
    print('Your grade is: B')

elif avg_grade >= 70:
    print('Your grade is: c')

elif avg_grade >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F') 


# TO DO: finish this
