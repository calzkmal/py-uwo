def do_something(text,c):
    dct = {}
    lst = text.split(c)
    words = lst
    for item in lst:
        dct[item] = (item.strip("s P"), len(words))
    
    group1 = []
    group2 = []
    for key in dct:
        group1.append(key.split()[0])
        group2.append(dct[key][0].split()[0])
    
    group1+=group2
    result = ''
    for item in group1:
        result += item
    return result

res = do_something("My Friends On Tuesdays Pick Plums", "e")
print(res)
