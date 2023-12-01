""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 19, 2023

"""

x = float(input("Please enter the temperature (in Celcius): ")) # Simple.
if x <= 0:
    print("At " + str(x) + ", the substance is in solid state.")
elif x <= 100:
    print("At " + str(x) + ", the substance is in liquid state.")
elif x > 100:
    print("At " + str(x) + ", the substance is in gas state.")
else:
    print("Error")