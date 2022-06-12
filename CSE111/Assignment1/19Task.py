def capitalize(string):
    if string != "":
        if chr(97) <= string[0] <= chr(122):
            capitalized_str = chr(ord(string[0]) - 32)
        else:
            capitalized_str = string[0]

        for index in range(1, len(string)):
            if (
                string[index - 1] == " "
                and string[index] == "i"
                and string[index + 1] == " "
            ):
                capitalized_str += "I"

            elif (
                string[index - 2] == "."
                or string[index - 2] == "!"
                or string[index - 2] == "?"
            ):
                capitalized_str += chr(ord(string[index]) - 32)

            else:
                capitalized_str += string[index]

        return capitalized_str

    else:
        return "Please enter a valid string."


user_input = input()
print(capitalize(user_input))