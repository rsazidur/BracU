def pass_check(password):
    # lower_count = sum(map(str.islower, password))
    # upper_count = sum(map(str.isupper, password))
    # digit_count = sum(map(str.isdigit, password))

    lower_count = 0
    for lower in password:
        if 97 <= ord(lower) <= 122:
            lower_count += 1

    upper_count = 0
    for upper in password:
        if 65 <= ord(upper) <= 90:
            upper_count += 1

    digit_count = 0
    for digit in password:
        if 48 <= ord(digit) <= 57:
            digit_count += 1

    spec_count = 0
    special_char = "_@$#"
    for spec in password:
        if spec in special_char:
            spec_count += 1

    error = ""
    if lower_count == 0:
        error += "Lowercase character missing"

    if upper_count == 0:
        if error != "":
            error += ", "
        error += "Uppercase character missing"

    if digit_count == 0:
        if error != "":
            error += ", "
        error += "Digit character is missing"

    if spec_count == 0:
        if error != "":
            error += ", "
        error += "Special character is missing"

    if error == "":
        print("OK")
    else:
        print(error)

user = input("Enter the password: ")
pass_check(user)