def my_function():

    for item in range(0, len(my_list) - 1):
        min_value = my_list[item]
        min_index = item
        for value in range(item, len(my_list)):
            if my_list[value] < min_value:
                min_value = my_list[value]
                min_index = value
        temp = min_value
        my_list[min_index] = my_list[item]
        my_list[item] = temp

        return my_list


my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
print(my_function())

# my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
#
# for item in range(0, len(my_list) - 1):
#     min_value = my_list[item]
#     min_index = item
#     for value in range(item, len(my_list)):
#         if my_list[value] < min_value:
#             min_value = my_list[value]
#             min_index = value
#     temp = min_value
#     my_list[min_index] = my_list[item]
#     my_list[item] = temp
# print(my_list)