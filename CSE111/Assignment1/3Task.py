def lower_sub(string):

    global new_str, start, end

    upper_count = 0
    for upper in string:
        if 65 <= ord(upper) <= 90:
            upper_count += 1

    # upper_count = sum(map(str.isupper, string))

    if upper_count == 2:
        for char in string:
            if 65 <= ord(char) <= 90:
                # if char.upper():
                start = string.find(char)
                new_str = string.replace(char, char.lower())
                break

        for char2 in new_str:
            if char2.isupper():
                end = new_str.find(char2)
                break

        sub = string[start + 1:end]
        if sub != "":
            print(sub)
        else:
            print("BLANK")

    else:
        print("Please, enter a valid input.")


user = input("Enter a Word: ")
lower_sub(user)