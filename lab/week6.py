text = open("text.txt", "r")
myfile = open("myfile.txt", "w") # Error 1
line = text.read() # Error 2, add () to make .read function work
words = line.split()
for word in words:
    print(word) # Error 3, remove unnecessary line
    myfile.write(word + "\n") # Error 4, add new line to separate the word

# Close the files
text.close()
myfile.close()