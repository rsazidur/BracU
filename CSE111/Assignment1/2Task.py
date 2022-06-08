def char_check(string):

    number_str = "0123456789"
    len_string = len(string)
    count = 0

    for item in string:
        if item in number_str:
            count += 1

    if count == len_string:
        return "NUMBER"
    elif count == 0:
        return "WORD"
    else:
        return "MIXED"

user = input("Enter a string: ")
result = char_check(user)
print(result)
