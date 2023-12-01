""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

minimum_age = 18
set_age = 0

while set_age < 1:
    age = int(input("\nPlease enter your age: "))
    if age >= 18:
        print("You can drive!")
    elif age == -1 or age < -1:
        break
    else:
        print("Sorry, you cannot drive") 
