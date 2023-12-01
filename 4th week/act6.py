""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

num = int(input("Please enter a number that is 1 or higher: "))
for i in range(0, num+1):
    if num < 1:
        print("Good Bye!")
        break
    if i % 2 != 0:
        print(f"{i}")