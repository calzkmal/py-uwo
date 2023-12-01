""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

num1 = int(input("Enter starting number of sequence: "))
num2 = int(input("Enter ending number of sequence: "))

for i in range(num1, num2+1):
    if i % 6 == 0: # if i % 2 == 0 and i % 3 == 0
        print(i)

