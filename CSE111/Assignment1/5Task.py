def pass_check(password):
    lower_count = sum(map(str.islower, password))
    upper_count = sum(map(str.isupper, password))
    digit_count = sum(map(str.isdigit, password))

    spec_count = 0
    special_char = "_@$#"
    for special_char in password:
        if special_char in password:
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