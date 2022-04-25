"""
# Lab Assignment 1

a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821),
           75717, [1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))

print(a_tuple[3][3])



# lab Assignment 2

given_tuple = (10, 20, 24, 25, 26, 35, 70)
print(given_tuple[2:-2])



# lab Assignment 3

books_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68, 821),
    ("Best Horror", "The Institute", 75, 717),
    ("Best History & Biography", "The five", 31, 783),
    ("Best Fiction", "The Testaments", 98, 291)
            )
print("Size of the tuple is:", len(book_info))
for book_info in books_info:
    print(book_info)


# lab Assignment 4

book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68821),
    ("Best Horror", "The Institute", 75717),
    ("Best History & Biography", "The five", 31783),
    ("Best Fiction", "The Testaments", 98291)
            )

for books in book_info:
    book_type, book_name, vote = books
    print(f"{book_name} won the {book_type} category with {vote} votes")



# lab Assignment 5

count = 0
given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
number = int(input("Enter a number to see how many time it appears in tuple: "))

for item in given_tuple:
    if item == number:
        count = count + 1

print(f"{number} appears {count} times in the tuple")


# lab Assignment 6

my_list = []

given_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

for item in given_tuple:
    my_list.append(item)

reverse_tuple = (my_list[::-1])

print(tuple(reverse_tuple))


# lab Assignment 7

boys = {'Harry': 15, 'Draco': 8, 'Nevil': 19}
girls = {'Ginnie': 18, 'Luna': 14}

boys_girls = boys.copy()
boys_girls.update(girls)
print(boys_girls)


# lab Assignment 8


dictionary = {}
summation = 0
times = int(input("Enter the number of elements: "))

for elements in range(times):
    key = input("Enter key: ")
    value = int(input("Enter Value: "))
    dictionary.update({key: value})
# print(dictionary)

for value in dictionary.values():
    summation = summation + value

# print(summation)
average = summation // times
print(f"Average is {average}")



# lab Assignment 9

exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165,
              'Pierre Cox': 190}

number = int(input("Enter your value: "))

dictionary = {key: value for key, value in exam_marks.items()if value >= number}
print(dictionary)



# lab Assignment 10

max_value = 0
max_key = ''
given_dict = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4,
              'adventure': 14}

for key, value in given_dict.items():
    if value > max_value:
        max_value = value
        max_key = key
print(f"The highest selling book genre is '{max_key}' and the number of books sold are {max_value}.")


# lab Assignment 11

file = str(input("Enter a string: ").lower())
counts = dict()

for line in file:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
print(counts)



# lab Assignment 12

dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count = 0
for value in dict_1.values():

    for number in value:
        count = count + 1

print(count)


# lab Assignment 13

list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

a_list = []
b_list = []
c_list = []

for item in range(len(list_1)):

    if list_1[item][0] == "a":
        a_list.append(list_1[item][1])

    elif list_1[item][0] == "b":
        b_list.append(list_1[item][1])

    else:
        c_list.append(list_1[item][1])

dictionary = {'a': a_list, 'b': b_list, 'c': c_list}
print(dictionary)


# lab ungraded Task 1

given_list = [(2, 3), (4, 5), (6, 7), (2, 8)]
new_list = []

for item in given_list:
    multiple = item[0] * item[1]
    new_list.append(multiple)

print(new_list)


# lab ungraded Task 2

a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
user = input("Enter any string or number: ")
new_list = []

for item in a_tuple:
    new_list.append(item[:-1] + [user])

print(tuple(new_list))


# lab ungraded Task 3

my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}

new_dictionary = {key: value for key, value in my_dictionary.items() if value is not None}

print(new_dictionary)


# lab ungraded Task 4

dict_1 = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}

lower_value = int(input("Enter a lower value: "))
upper_value = int(input("Enter a upper value: "))

new_dictionary = {key: value for (key, value) in dict_1.items()if lower_value <= value < upper_value}
print(new_dictionary)


"""
# lab ungraded Task 5

# given_list = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
#
# dictionary = {}
#
# for key, value in given_list:
#     if value == value[1]:


# lab ungraded Task 6
