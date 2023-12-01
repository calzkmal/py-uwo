"""
CS1026A 2023
Assignment 01 Project 01 - Part A
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
September 19, 2023
"""

print("Project One (01) - Part A : Fibonacci Sequence")
end_sequence = int(input("Sequence ends at: ")) # Get the input on the end of the sequence
loop_variable = 0 # Specify the value "loop_variable" that will be used in loop
value_1 = 0 # Specify the value "value_1" that acts as loop variable 1
value_2 = 1 # Specify the value "value_2" that acts as loop variable 2

while loop_variable <= end_sequence: # Start the loop
    if loop_variable == 0: # If the "loop_variable" == 0
        print(f"{loop_variable}:  {0} {0}") # Print the amount of 0 0
    elif loop_variable == 1: # If the "loop_variable" == 1
        print(f"{loop_variable}:  {1} {1}") # Print the amount of 1 1
    else: # If "loop_variable" is not with all mentioned above
        value_result = value_1 + value_2 # Assign the result of iteration with "value_1" and "value_2" to "value_result"
        print(f"{loop_variable}:  {value_result} {value_result:1,}") # Print the formatted result
        value_1, value_2 = value_2, value_result # Assign the new value of "value_2" to "value_1", and new value of "value_result" to "value_2"
    loop_variable += 1 # Iterates "loop_variable" to continue the loop
    
print("\nEND: Project One (01) - Part A")
print("Calzy Akmal Indyramdhani cindyram 251397118")
