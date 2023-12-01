""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = input("Please enter your full name: ") # Ask for user input
y = x.split(" ") # Split the string based on space between them
first_name = y[0] # Get the first letter of the first name
last_name = y[-1] # Get the last letter of the last name

if len(y) >= 2: # If the length of the splitted string is more than 2 substring
    print("First letter: " + first_name[0] + ", Last letter: " + last_name[-1]) # Print the first letter of the first name and last letter of last name
else:
    print("Please enter a full name with at least two parts.") # Print if the condition not met
