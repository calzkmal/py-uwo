values = [1,2,3,4,5]
newValues = list(values) # Error 1
for i in range(len(values)): # Error 2
    newValues[i] += 1 # Error 3
    print("Old Value at index {} is: {} ".format(i, values[i])) # Error 4
    print("New Value at index {} is: {} \n".format(i, newValues[i]))