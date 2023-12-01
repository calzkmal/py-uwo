""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = int(input("Please enter your age: ")) # Ask the user age
if x >= 18: # If the age is 18 or greater
    y = input("Do you have an account? (yes/no): ") # Ask whether the user has an account or not
    if "yes" in y.lower(): # If yes
        print("You have full access to all features.") # Print
    elif "no" in y.lower(): # If no
        print("You can create an account to access all features.") # Print
    else: # If neither
        print("You can only answer with a 'yes' or 'no'.") # Print
else: # If the age is less than 18
    y = input("Do you have an account? (yes/no): ")
    if "yes" in y.lower():
        print("You have limited access to certain features.")
    elif "no" in y.lower():
        print("You need to be 18 or older and create an account to access all features.")
    else:
        print("You can only answer with a 'yes' or 'no'.")