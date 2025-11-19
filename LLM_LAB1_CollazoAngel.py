# Simple Quiz Game in Python
#Angel Collazo

#November 18,2025

#LLM_LAB1

#This program will asks 3 questions to the user
#This program will use input() to get the player’s response.
#Answers are checked with .strip().lower() to ignore spaces and capitalization.
#A score counter keeps track of correct answers.
#At the end, the player sees their total score with a little feedback.


def quiz_game():
    print("Welcome to the Quiz Game!")
    score = 0

    #User will answer the first question(What is the capital of France?).
    answer1 = input("Q1: What is the capital of France? ")
    if answer1.strip().lower() == "paris":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Paris.")

    #User will answer the second question(What is 5 * 6?).
    answer2 = input("Q2: What is 5 * 6? ")
    if answer2.strip() == "30":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is 30.")

    #User will answer the third Question(Who developed the Python programming language?).
    answer3 = input("Q3: Who developed the Python programming language? ")
    if answer3.strip().lower() == "guido van rossum":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is Guido van Rossum.")

    # The Program will produce a feedback according with the answers of the user.
    print(f"\nYou got {score} out of 3 questions correct!")
    if score == 3:
        print("Excellent job! 🎉")
    elif score == 2:
        print("Good work! 👍")
    else:
        print("Better luck next time! 💡")

# Run the game
quiz_game()


# Reflect on the Experience

#I think it was Amazing what this tool can do, the code didnt have errors but you can notice that it was not a person because
#on the comments was generic( for example like a Text book).The parts that I have to improve was the comments.I could improve the promt by maybe writing
#more in detail how i want the comments.I think is a useful tool but still lack kind of the human touch in coding, I can say defenetly smarter than me.
#The prompt I use was to create a question game with three questions in python Language.
