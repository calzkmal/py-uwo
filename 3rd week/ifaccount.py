""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = float(input("Please enter your account balance: $")) # Get the user input for account balance and change it to float
y = float(input("Enter the amount you want to withdraw: $")) # Get the user input for withdrawal amount and change it to float
z = x - y # New amount of balance after withdrawal

if y <= x: # If the withdrawal amount is less or the same as the account balance
    print("Withdrawal successful! Your new balance is $" + str(z)) # Print the new balance
else: # When the condition not met
    print("Insufficient funds. Withdrawal not possible.") # Print a string saying withdrawal not possible
