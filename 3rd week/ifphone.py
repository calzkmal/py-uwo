""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = input("Please enter a 10-digit phone number: ") # Basic
if x.startswith("226"): # Check if input starts with 226
    if len(x) == 10: # Check if length of input is equals to 10
        if x.isdigit(): # Check if input is all number
            # Formatted number explanation: {x[:3]} = takes the 3 first character
            # {x[3:6]} takes the 3-6th character
            # {x[6:]} takes the 6th to last character
            print("Valid phone number: " + str(f"({x[:3]}) {x[3:6]}-{x[6:]}"))
        else:
            print("Not a number!") 
    else:
        print("Invalid length!")
elif x.isalpha(): # Check if input is not number
    print("Not a number!")
else:
    print("Does not start with 226!")