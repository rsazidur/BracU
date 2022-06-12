def combine_dictionaries(dict_1, dict_2):

    combined_dict = {}

    for key in dict_1:
        if key in dict_2:
            new_value = dict_1[key] + dict_2[key]
        else:
            new_value = dict_1[key]

        combined_dict[key] = new_value

    for key in dict_2:
        if key not in combined_dict:
            combined_dict[key] = dict_2[key]

    return combined_dict


str_input_1 = input()
str_input_2 = input()

dict_1 = dict(
    (x.strip(), int(y.strip()))
    for x, y in (element.split(":") for element in str_input_1.split(", "))
)

dict_2 = dict(
    (x.strip(), int(y.strip()))
    for x, y in (element.split(":") for element in str_input_2.split(", "))
)

result = combine_dictionaries(dict_1, dict_2)
unique_value = tuple(
    sorted(set(result[value] for value in result)))
print(result)
print(f"Values: {unique_value}")