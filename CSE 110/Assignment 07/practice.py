# bubble sort
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for idx in range(len(my_list)):
    for idx_2 in range(len(my_list) - 1):
        if my_list[idx_2] > my_list[idx_2 + 1]:
            temp = my_list[idx_2]
            my_list[idx_2] = my_list[idx_2 + 1]
            my_list[idx_2 + 1] = temp

print(my_list)

my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

for idx in range(len(my_list) - 1, 0, - 1):
    for idx_2 in range(len(my_list) - 1):
        if my_list[idx_2] > my_list[idx_2 + 1]:
            temp = my_list[idx_2]
            my_list[idx_2] = my_list[idx_2 + 1]
            my_list[idx_2 + 1] = temp

print(my_list)


# bubble sort

def bubble_sort():
    for idx in range(len(my_list)):
        for idx_2 in range(idx + 1, len(my_list)):

            if my_list[idx] > my_list[idx_2]:
                temp = my_list[idx]
                my_list[idx] = my_list[idx_2]
                my_list[idx_2] = temp

    return my_list


my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
print(bubble_sort())

# selection sort

