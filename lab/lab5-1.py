the_list = []

while len(the_list) < 10:
    user_input = int(input("Input number: "))
    if user_input not in the_list:
        the_list.append(user_input)
    else:
        break
print(the_list)