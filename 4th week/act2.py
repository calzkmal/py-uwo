""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

sum = 0
num = int(input("Please enter a number from zero or higher: "))
for i in range(0, num+1):
    sum += i
print(f"Sum from 0 to {num} is {sum}")