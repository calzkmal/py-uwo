def countVowels(word):
    numVowels = 0
    for letter in word.lower():
        if letter in "aeiou":
            numVowels+=1
    return numVowels

print(countVowels("AEIOu"))