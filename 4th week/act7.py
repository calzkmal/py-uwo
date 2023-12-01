""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

pw = input("Enter a password: ")
errors = []

if not any(char in "!@#$%^&*_-()" for char in pw):
    errors.append("Password must have a special character.")
if not any(char.isdigit() for char in pw):
    errors.append("Password must have at least one digit.")
if not any(char.isupper() for char in pw):
    errors.append("Password must have at least one upper case letter.")
if not any(char.islower() for char in pw):
    errors.append("Password must have at least one lower case letter.")
if len(pw) < 10:
    errors.append("Password must have at least 10 characters.")

if errors:
    print("Password is not valid!")
    for error in errors:
        print(error)
else:
    print("Password is valid.")