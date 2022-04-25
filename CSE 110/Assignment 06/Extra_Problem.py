"""
# Practice problem task 1.

def function_name():
    empty_list = []
    string_name = (input('Please, enter a string: '))
    for name in string_name:
        if name not in empty_list:
            new_string = str(ord(name)) + name\
                         + str(ord(name))
            empty_list.append(new_string)
    return empty_list

print(function_name())



# Practice problem task 2.

def function_name():
    string_name = (input('Please, enter a string: '))
    empty = {}
    for item in string_name:
        name = [string_name.index(item), string_name.index(item) - len(string_name)]
        empty[item] = name
    print(empty)


print(function_name())

"""

# Practice problem task 3.