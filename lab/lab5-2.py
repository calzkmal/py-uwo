def count_str(str):
    count = 0
    for i in str:
        if len(i) >= 2 and i[0] == i[-1]:
            count+=1
    return count

ex_list = ['bgh', 'wer', 'yuy', '1661']

print(count_str(ex_list))