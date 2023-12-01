"""
CS1026A 2023
Lab 8 - Practical Exercises 1
Calzy Akmal Indyramdhani
251397118
cindyram@uwo.ca
November 17, 2023
"""

num_set = {
    'even': set(), 
    'odd': set(),
    'three': set()
    }

for num in range(0,20):
    if num % 2 == 0:
        num_set['even'].add(num)
    if num % 2 == 1:
        num_set['odd'].add(num)
    if num % 3 == 0:
        num_set['three'].add(num)

for key, value in num_set.items():
    print(f"{key}: {value}")