"""
# 1todo - Bubble sort starts arranging the elements from the top
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]

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
print(my_list)

# 2todo Selection sort starts arranging the elements from the bottom
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for item in range(len(my_list)):
    min_value = my_list[item]
    min_index = item
    for value in range(item + 1, len(my_list)):
        if my_list[value] < min_value:
            min_value = my_list[value]
            min_index = value
    temp = my_list[min_index]
    my_list[min_index] = my_list[item]
    my_list[item] = temp
print(my_list)

# 3todo
my_list = [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for item in range(0, len(my_list) - 1):
    max_value = my_list[item]
    max_index = item
    for value in range(item, len(my_list)):
        if my_list[value] > max_value:
            max_value = my_list[value]
            max_index = value
    temp = max_value
    my_list[max_index] = my_list[item]
    my_list[item] = temp
print(my_list)

# 4todo
sitting_list = [10, 30, 20, 70, 11, 15, 22, 16, 58, 100, 12, 56, 70, 80]
list1 = []
list2 = []
sorted_list = []
counter1 = 0
counter2 = 0
for even_index in range(0, len(sitting_list), 2):
    list1.append(sitting_list[even_index])
for odd_index in range(1, len(sitting_list), 2):
    list2.append(sitting_list[odd_index])
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2, reverse=True)

for i in range(len(sitting_list)):
    if i % 2 == 0:
        sorted_list.append(sorted_list1[counter1])
        counter1 += 1
    else:
        sorted_list.append(sorted_list2[counter2])
        counter2 += 1
print(sorted_list)

"""
# 5todo
Lst = [['Alan', 95, 87, 91], ['Turing', 92, 90, 83], ['Elon', 87, 92, 80], ['Musk', 85, 94, 90]]
L = ['CSE110', 'PHY111', 'MAT110']
user_input = str(input())
if user_input == 'CSE110':
    index = 1
elif user_input == 'PHY111':
    index = 2
elif user_input == 'MAT110':
    index = 3
a_dict = {}
list1 = []
for item in range(len(Lst)):
    a_dict.update({Lst[item][index]: Lst[item][0]})
    list1.append(Lst[item][index])
a = sorted(list1, reverse=True)
for value in a:
    print(a_dict[value])

# 6todo
My_list = [4, 2, 3, 1, 6, 5]
counter = 0
for item in range(len(My_list)):
    min = My_list[item]
    min_index = item
    for value in range(item + 1, len(My_list)):
        if My_list[item] > value:
            min = My_list[value]
            min_index = value
            counter += 1
    temp = value
    My_list[value] = My_list[item]
    My_list[item] = temp
print(counter)

# 7todo
list_one = []
list_two = []
element1 = int(input('Element no for 1st list: '))
element2 = int(input('Element no for 2nd list: '))
for i in range(0, element1):
    i = int(input('Enter element for first list: '))
    list_one.append(i)
for j in range(0, element2):
    j = int(input('Enter element for second list: '))
    list_one.append(j)
new_list = list_one + list_two
sorted_newlist = sorted(new_list)
print('Sorted list=', sorted_newlist)
length = len(sorted_newlist)

if length % 2 != 0:
    num = int((length + 1) / 2)

    print('Median=', sorted_newlist[num - 1])
else:
    index = int((length) // 2) - 1
    print(index)
    index1 = int(((length) / 2) + 1)
    print(index1)
    median = float((sorted_newlist[index] + sorted_newlist[index1]) / 2)
    print('Median=', median)

# 8todo
list_one = [-10, 15, 2, 4, -4, 7, -8]
neg = []
pos = []
for i in list_one:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
a = 0
b = 0
diff = 1000000
for j in range(0, len(neg)):
    minimum = pos[0] + neg[j]
    if diff > minimum:
        diff = minimum
    for k in range(0, len(pos)):
        min = pos[k] + neg[j]
        min = abs(min)
        if min < diff:
            a = neg[j]
            b = pos[k]
            diff = min
print(a, b)
