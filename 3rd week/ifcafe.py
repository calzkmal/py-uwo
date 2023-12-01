""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = input("What would you like to order? ") # Ask the user about input on what to order

if "coffee" in x.lower(): # Check if the user ask for coffee
    y = int(input("Please enter your age: ")) # Ask the user about their age
    if y >= 10: # If the age is 10 or more
        print(x + " will be served.") # Print the coffee will be served
    else: # If the user is too young
        print("Sorry, you are too young to order coffee. Please consider another option") # Print
else: # If the order is not coffee
    print(x + " will be served.") # Print