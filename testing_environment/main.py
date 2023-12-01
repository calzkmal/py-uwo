def difflist(lst):
    newList = []
    for i in range(1, len(lst)) :
        n = lst[i-1]
        m = lst[i]
        newList.append(m-n)
    return newList

myList = [1,2,7,101,127]

print(difflist(myList))