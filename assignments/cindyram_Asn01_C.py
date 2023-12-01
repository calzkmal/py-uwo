"""
CS1026A 2023
Assignment 01 Project 01 - Part C
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
September 29, 2023
"""

print("Project One (01) - Part C: The Moore the Merrier")
start_transistor = int(input("Starting Number of transistors: ")) # Get the user input for starting transistors
start_year = int(input("Starting Year: ")) # Get the user input for starting year
number_of_year = int(input("Total Number of Year: ")) # Get the user input for total number of year

current_year = start_year # Set the value of "current_year" with the value of "start_year"
current_transistors = start_transistor # Set the value of "current_transistors" with the value of "start_transistors"
computer_flops_original = 0 # Set the value of "computer_flops_original" with 0

print("\nYEAR : TRANSISTORS : FLOPS :")

for year in range(start_year,start_year+(number_of_year+2),2): # Start the loop using "year" variable for each year within the specified range, with the starting year represented by start_year and the ending year represented by start_year + (number_of_year + 2). The loop will increment by 2 years in each iteration.
    computer_flops = current_transistors * 50 # Get the amount of flops by multiplying the amount of "current_transistors" by 50  
    
    if computer_flops < 1000: # If the amount of "computer_flops" is less than 1,000
        computer_variable = "FLOPS" # Set the value of "computer_variable" to "FLOPS"
        computer_flops_original = int(computer_flops) # Set the value of "computer_flops_original" to the integer value of "computer_flops"
    
    elif 1000 <= computer_flops < 1000000: # If the amount of "computer_flops" is between 1,000 and 1,000,000
        computer_variable = "kiloFLOPS" # Set the value of "computer_variable" to "kiloFLOPS"
        computer_flops/=1000 # Divide the value of "computer_flops" by 1,000 to represent it in thousands
        computer_flops_original = int(computer_flops * 1000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000 as an integer
    
    elif 1000000 <= computer_flops < 1000000000: # If the amount "computer_flops" is between 1,000,000 and 1,000,000,000
        computer_variable = "megaFLOPS" # Set the value of "computer_variable" to "megaFLOPS"
        computer_flops/=1000000 # Divide the value of "computer_flops" by 1,000,000 to represent it in millions
        computer_flops_original = int(computer_flops * 1000000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000 as an integer
   
    elif 1000000000 <= computer_flops < 1000000000000: # If the amount "computer_flops" is between 1,000,000,000 and 1,000,000,000,000
        computer_variable = "gigaFLOPS" # Set the value of "computer_variable" to "gigaFLOPS"
        computer_flops/=1000000000 # Divide the value of "computer_flops" by 1,000,000,000 to represent it in billions
        computer_flops_original = int(computer_flops * 1000000000)  # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000 as an integer
   
    elif 1000000000000 <= computer_flops < 1000000000000000: # If the amount of "computer_flops" is between 1,000,000,000,000 and 1,000,000,000,000,000
        computer_variable = "teraFLOPS" # Set the value of "computer_variable" to "teraFLOPS"
        computer_flops/=1000000000000 # Divide the value of "computer_flops" by 1,000,000,000,000 to represent it in trillions
        computer_flops_original = int(computer_flops * 1000000000000)  # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000,000 as an integer
   
    elif 1000000000000000 <= computer_flops < 1000000000000000000: # If the amount "computer_flops" is between 1,000,000,000,000,000 and 1,000,000,000,000,000,000
        computer_variable = "petaFLOPS" # Set the value of "computer_variable" to "petaFLOPS"
        computer_flops/=1000000000000000 # Divide the value of "computer_flops" by 1,000,000,000,000,000 to represent it in quadrillions
        computer_flops_original = int(computer_flops * 1000000000000000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000,000,000 as an integer
   
    elif 1000000000000000000 <= computer_flops < 1000000000000000000000: # If the amount "computer_flops" is between 1,000,000,000,000,000,000 and 1,000,000,000,000,000,000,000
        computer_variable = "exaFLOPS" # Set the value of "computer_variable" to "exaFLOPS"
        computer_flops/=1000000000000000000 # Divide the value of "computer_flops" by 1,000,000,000,000,000,000 to represent it in quintillions
        computer_flops_original = int(computer_flops * 1000000000000000000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000,000,000,000 as an integer
   
    elif 1000000000000000000000 <= computer_flops < 10000000000000000000000000: # If the amount "computer_flops" is between 1,000,000,000,000,000,000,000 and 10,000,000,000,000,000,000,000
        computer_variable = "zettaFLOPS" # Set the value of "computer_variable" to "zettaFLOPS"
        computer_flops/=1000000000000000000000 # Divide the value of "computer_flops" by 1,000,000,000,000,000,000,000 to represent it in sextillions
        computer_flops_original = int(computer_flops * 1000000000000000000000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000,000,000,000,000 as an integer
   
    elif 1000000000000000000000000 <= computer_flops < 1000000000000000000000000000: # If the amount "computer_flops" is between 10,000,000,000,000,000,000,000 and 1,000,000,000,000,000,000,000,000
        computer_variable = "yottaFLOPS" # Set the value of "computer_variable" to "yottaFLOPS"
        computer_flops/=1000000000000000000000000 # Divide the value of "computer_flops" by 1,000,000,000,000,000,000,000,000 to represent it in septillions
        computer_flops_original = int(computer_flops * 1000000000000000000000000) # Set the value of "computer_flops_original" to the value of "computer_flops" multiplied by 1,000,000,000,000,000,000,000,000 as an integer

    computer_flops_formatted = f"{computer_flops:,.2f}" # Set the value of "computer_flops_formatted" with 2 numbers behind 0

    # Print the year, the number of transistors (with comma separators), the formatted computer processing power, its unit (e.g., "kiloFLOPS"), and the original computer processing power (with comma separators)
    print(f"{year} {start_transistor:,} {computer_flops_formatted:} {computer_variable} {computer_flops_original:,}")

    current_transistors*=2 # Double the amount of "current_transistors" to continue the loop process
    start_transistor*=2 # Double the amount of "start_transistors" to continue looping from the first transistors amount

print("\nEND: Project One (01) - Part C")
print("Calzy Akmal Indyramdhani cindyram 251397118")