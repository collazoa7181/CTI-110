#Angel Collazo

#November 7, 2025

#P4HW1

# This program collects test scores using a loop, validates input,
# drops the lowest score, calculates the average, and assigns a letter grade.

#Github Link:

#Ask user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))


scores = []

#Collect the scores
for Score in range(1, num_scores + 1):
    score = float(input(f"Enter score #{Score}: "))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{Score} again: "))
    scores.append(score)

#Process the results
lowest_score = min(scores)
modified_scores = scores.copy()
modified_scores.remove(lowest_score)
average_score = sum(modified_scores) / len(modified_scores)

#Determine the letter for the grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

#Display results
print("\n----------------Results----------------")
print(f"Lowest Score  : {lowest_score:.2f}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {grade}")
print("---------------------------------------")





#Pseudocode
#The program will ask the user how many scores they want to enter
#The program evaluate if the score is valid, it should be between 0 and 100 . 
#If it is not, the program will notify the user and ask for a VALID score to be entered.
#The program will collect the scores
#The program will process the results and determine the letter grade corresponding to the number
#The program will display results
      
