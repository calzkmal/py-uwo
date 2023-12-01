""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = input("Please enter your grade: ") # Yeah, it's so simple
if "A" in x.upper():
    print("Excellent! You've got an 'A'.")
elif "B" in x.upper():
    print("Good job! You've got a 'B'.")
elif "C" in x.upper():
    print("Not bad! You've got a 'C'.")
elif "D" in x.upper():
    print("You passed. You've got a 'D.")
elif "F" in x.upper():
    print("Unfortunately, you failed. You've got an 'F'.")
else:
    print("Invalid input. Please enter a valid grade (A, B, C, D, or F).")
