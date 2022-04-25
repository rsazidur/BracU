"""
# task 1

new_list = []

for item in range(1, 6):
    number = int(input("Enter your number: "))
    new_list.append(number)
    print(f"Numbers in the list: {new_list}")

# task 2
empty_list = []
user = int(input("How many list you want to create: "))

if user > 3:

    for number in range(0, user):
        num = int(input(">>> "))
        empty_list.append(num)
    print(empty_list[2:-2])

else:
    print("Not possible"


# task 3

empty_list = []

print("Sir, please enter your five desire number.")
for number in range(0, 5):
    num = int(input(">>> "))
    empty_list.append(num)

for index in range(-1, -6, -1):
    print(empty_list[index])



# task 4

given_list = [1, 2, 3, 4, 5, 6, 7]
empty_list = []

for index in range(0, len(given_list)):
    empty_list.append(given_list[index] * given_list[index])
print("Given list: ", given_list)
print("Output list:", empty_list)



# task 5

given_list = ["hey", "there", "", "what's", "", "up", "", "?"]
print('Original List:', given_list)
copied_list = given_list

for item in given_list:
    if item == "":
        copied_list.remove(item)
print("Modified List:", copied_list)


# task 6

user = str(input("Sir, please enter your seven desire number:"))
user_list = [int(number) for number in user.split(',')]
new_list = user_list[0:7]
print("My list: ", new_list)

max_num = new_list[0]

for item in new_list:
    if item > max_num:
        max_num = item

value = new_list.index(max_num)
print(f"Largest number in the list is {max_num} which was found at index {value}.")

# task 7

list_one = [1, 3, 5, 7, 9, 10]
list_two = [2, 4, 6, 8]

print(list_one[0:len(list_one)-1] + list_two)

# task 8

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]

new_list = []

for item in range(len(list_one)):
    if list_one[item] % 2 == 0:
        new_list.append(list_one[item])

for item in range(len(list_two)):
    if list_two[item] % 2 == 0:
        new_list.append(list_two[item])

print(new_list)

# task 9

user = input(str("Sir, Please enter your number: "))
empty_list = []
value = " "
for number in user:
    if number != " ":
        value = value + number
    else:
        empty_list.append(int(value))
        value = " "
empty_list.append(int(value))
print("Original list: ", empty_list)

empty_list2 = []

for item in empty_list:
    if item % 2 == 1:
        empty_list2.append(item)
print("Modified list: ", empty_list2)

# task 10


user = str(input("Sir, please enter your seven desire number:"))
user_list = [int(number) for number in user.split(',')]

print("Input list: ", user_list)

empty_list = []

for number2 in user_list:
    if number2 not in empty_list:
        empty_list.append(number2)
print("Modified list: ", empty_list)



# task 11

list_one = [1, 4, 3, 2, 6]
list_two = [5, 6, 9, 8, 7]

flag = False

for index in list_one:
    if index in list_two:
        flag = True
        break
print(flag)



# task 12 ( Bug, if index 0 is greater than index 1 the code don't check every value.)

user = input("Sir, Please enter your desire number(seperated by comma: ")
user_list = [int(number) for number in user.split(",")]
new_list = user_list[0:7]
print("My list: ", new_list)

if new_list[0] > new_list[1]:
    max_1, max_2 = new_list[0], new_list[1]
else:
    max_1, max_2 = new_list[1], new_list[0]
    for item in new_list[2:]:
        if item > max_2:
            if item > max_1:
                max_2, max_1 = max_1, item
            else:
                max_2 = item
print(max_2)



# task 12

user = input("Sir, Please enter your desire number(seperated by comma: ")
user_list = [int(number) for number in user.split(",")]
new_list = user_list[0:7]
print("My list: ", new_list)

max_num = new_list[0]
for item in new_list:
    if item > max_num:
        max_num = item

print(max_num)

sec_max_num = new_list[0]
for item2 in new_list:
    if item2 > sec_max_num:
        if item2 != max_num:
            sec_max_num = item2

print(sec_max_num)



# task 12 using sort function

user = input("Sir, Please enter your desire number(seperated by comma: ")
user_list = [int(number) for number in user.split(",")]
new_list = user_list[0:7]
print("My list: ", new_list)

new_list.sort()
print("My list 2: ", new_list)

new_list2 = sorted(new_list)
print(new_list2[-2:-1])



# task 13

new_list = []
print("Sir, Please enter your desire number.")
for number in range(0, 5):
    num = int(input(">>> "))
    new_list.append(num)
print("New list: ", new_list)

max_num = new_list[0]
for item in new_list:
    if item > max_num:
        max_num = item
print("Maximum Number:", max_num)
min_num = new_list[0]
for item in new_list:
    if item < min_num:
        min_num = item
print("Minimum Number:", min_num)



# task 15

empty_list_1 = []
empty_list_2 = []

list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

for item in list_one:
    if item not in empty_list_1:
        empty_list_1.append(item)
print(empty_list_1)


for item in list_two:
    if item not in empty_list_2:
        empty_list_2.append(item)
print(empty_list_2)

empty_list_1.extend(empty_list_2)

final_list = []

for item in empty_list_1:
    if item not in final_list:
        final_list.append(item)

print(sorted(final_list))


# find the minimum to maximum in the list...

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for num in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList.append(value)

for item in range(Number):
    for item2 in range(item + 1, Number):
        if NumList[item] > NumList[item2]:
            temp = NumList[item]
            NumList[item] = NumList[item2]
            NumList[item2] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)

"""