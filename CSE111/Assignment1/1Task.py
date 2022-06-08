def case_conversion(string):

    upper_case = ""
    lower_case = ""

    for char in string:
        if 65 <= ord(char) <= 90:
            upper_case += char
        else:
            lower_case += char

    upper_count = len(upper_case)
    lower_count = len(lower_case)

    if upper_count > lower_count:
        return string.upper()
    else:
        return string.lower()


user = input("Enter a string: ")
result = case_conversion(user)
print(result)