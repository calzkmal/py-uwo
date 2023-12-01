"""
CS1026A 2023
Assignment 01 Project 01 - Part B
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
September 23, 2023
"""

def prime_printer(starting_param,final_param): # Initiates a function to start printing the prime numbers, and take 2 parameters "starting_param" and "final_param"
    print(f"\nPrime numbers in the range from: {starting_param} and {final_param} are:  ") # Print the title 
    for number in range (starting_param,final_param+1): # Starts the iteration between number "starting_param" and "final_param"
        if number > 1: # Because number less or equal than 1 is not a prime number
            for divider in range (2, number): # Starts the iteration to check all possible number from 2 to "number"
                if (number % divider) == 0: # If the number is divisible with "divider" and there's no remainder, it is not a prime 
                    break # Stop the iteration
            else: # If 'number' is not divideable with 'divider'
                print(f"{number} is prime") # Print the number and tells that it is a prime
    return ("\nEnd Part One - Project B") # Return a value so it will not says "None"

print("Part One - Project B: Prime Choice")

starting_number = int(input("\nPrime Numbers starting with: ")) # Get the first value
final_number = int(input("and ending with: ")) # Get the second value
if starting_number < 1: # If the "starting_number" is less than 1
    print("There cannot be number less than 1.")
elif final_number < 1: # If the "final_number" is less than 1
    print("There cannot be number less than 1.")
elif starting_number == final_number: # If the "starting_number" and "final_number" are equals
    print("The value of the first and second variable cannot be the same.")
elif final_number < starting_number: # If the "final_number" is greater than "starting_number"
    print(f"\nIncorrect input: {starting_number} is greater than {final_number}")
    print("The numbers have been automatically switch.") 
    starting_number, final_number = final_number, starting_number # Switch the "final_number" and "starting_number" value
    print(prime_printer(starting_number,final_number)) # Calls the function with "starting_number" and "final_number" as parameter
    print("Calzy Akmal Indyramdhani cindyram 251397118")
else:
    print(prime_printer(starting_number,final_number)) # Calls the function with "starting_number" and "final_number" as parameter
    print("Calzy Akmal Indyramdhani cindyram 251397118")
