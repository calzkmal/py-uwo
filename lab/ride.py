"""
CS1026A 2023
Lab 02
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
September 25, 2023
"""

age = int(input("Enter your age: "))
if age >= 9:
    height = float(input("Enter your height in cm: "))
    if height > 130:
        print("You may go on this ride!")
    else:
        print("You are too short for this ride.")
else:
    print("You are too young for this ride.")