""" 

Author: Calzy Akmal Indyramdhani
Student ID: 251397118
Date Created: September 26, 2023

"""

word = input("Please enter a word: ")
vowels = "aeiou"

for char in word: 
    if char.lower() in vowels:
        print(f"Count of {vowels[0]} is {word.count(vowels[0])}")
        print(f"Count of {vowels[1]} is {word.count(vowels[1])}")
        print(f"Count of {vowels[2]} is {word.count(vowels[2])}")
        print(f"Count of {vowels[3]} is {word.count(vowels[3])}")
        print(f"Count of {vowels[4]} is {word.count(vowels[4])}")
        break