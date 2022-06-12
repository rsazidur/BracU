def invert(dictionary):

    dict = {}
    for item1, item2 in dictionary.items():
        if item2 in dict:
            dict[item2] = dict[item2] + [item1]
        else:
            dict[item2] = [item1]

    return dict


str_input = (
    input()
)

dictionary = dict(
    (x.strip(), y.strip())
    for x, y in (item.split(":") for item in str_input.split(", "))
)

result = invert(dictionary)
print(result)