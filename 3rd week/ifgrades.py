""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = float(input("Enter the first grade: ")) # Takes the first grade and save it as float
y = float(input("Enter the second grade: ")) # Takes the second grade and save it as float


if x > y: # If first grade is greater than second grade
    print("Grades in ascending order: " + str(y) + ", " + str(x)) # Print 
elif y > x: # If the second grade is greater than first grade
    print("Grades in ascending order: " + str(x) + ", " + str(y)) # Print
else: # If other condition
    print("Grades in ascending order: " + str(x) + ", " + str(y)) # Just print.