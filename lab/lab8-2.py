sentence = "I had such a horrible day It was awful so bad sigh It could not have been worse but actually though it was such a terrible horrible awful bad day"

makeItHappy = {"horrible": "amazing", "bad": "good", "awful": "awesome", "worse": "better", "terrible": "great"}

spsentence = sentence.split()
for word in range (0, len(spsentence)-1): # Error 1
    if spsentence[word] in makeItHappy:
        spsentence[word] = makeItHappy[spsentence[word]] # Error 2

newString = ""

for word in spsentence:
    newString = newString + word + " "

print(newString)