"""
# task 1

def even_checker(Number):
    if Number % 2 == 0:
        print("Even!!")
    else:
        print("Odd!!")

even_checker(2)

# task 2

def function_name(limit):
    list1 = [0, 1]
    while True:
        new_number = list1[-1] + list1[-2]
        if new_number <= limit:
            list1.append(new_number)
        else:
            break

    return list1

print(*function_name(10))

# task 2 another way...(like we did in assignment 2)

def fibonacci(Number):
    first_num = 0
    second_num = 1
    for num in range(0, Number):

        if Number <= 1:
            Next = num
        else:
            Next = first_num + second_num
            first_num = second_num
            second_num = Next

        print(Next, end=" ")

fibonacci(6)


# task 2 using return function...

def fibonacci(Number):
    if Number <= 1:
        return Number
    else:
        return fibonacci(Number - 1) + fibonacci(Number - 2)

terms = int(input("Enter the Limit? "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for num in range(terms):
        print(fibonacci(num), end=" ")



# task 2 another way for better understanding...

def fibonacci(Number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

number = int(input("Enter the Range Number: "))
for n in range(0, number):
    print(fibonacci(n))

# task 3 (using return function)

def foo_moo(number):
    if number % 2 == 0:
        return "Foo"
    elif number % 3 == 0:
        return "Boo"
    elif number % 2 and number % 3 == 0:
        return "FooMoo"
    else:
        return "Boo"

print(foo_moo(5))

# task 3 (when you ask an input from user)

def foo_moo():
    number = int(input("Sir, please enter a number: "))
    if number % 2 == 0:
        print("Foo")
    elif number % 3 == 0:
        print("Boo")
    elif number % 2 and number % 3 == 0:
        print("FooMoo")
    else:
        print("Boo")

foo_moo()


# task 3 another way

def foo_moo(number):
    if number % 2 == 0:
        print("Foo")
    elif number % 3 == 0:
        print("Boo")
    elif number % 2 and number % 3 == 0:
        print("FooMoo")
    else:
        print("Boo")

foo_moo(5)


# task 4 ( using isupper method)

def function_name():
    upper_count = 0
    lower_count = 0
    user = str(input("Enter a string: "))
    for char in user:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Uppercase characters : ", upper_count)
    print("No. of lower characters :", lower_count)

function_name()


# task 4 using ASCII value...

def function_count(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if 65 <= ord(char) <= 90:
            upper_count += 1
        elif 97 <= ord(char) <= 122:
            lower_count += 1
    print("No. of Uppercase characters :", upper_count)
    print("No. of Lowercase Characters :", lower_count)

function_count("The quick Sand Man")

# task 4 using is true...

def function_name():
    upper_count = 0
    lower_count = 0
    user = str(input("Enter a string: "))
    for char in user:
        if char == char.upper():
            upper_count += 1
        elif char == char.lower():
            lower_count += 1
    print("No. of Uppercase characters : ", upper_count)
    print("No. of lower characters :", lower_count)

function_name()


# task 5 (asking input from user)

def calculate_tax():
    age = int(input("Enter user age: "))
    salary = int(input("Enter user salary: "))
    current_job = str(input("Enter your current position: ").lower())
    if age < 18 or salary < 10000 or current_job == "president":
        print("0")
    elif 10000 < salary < 20000:
        value1 = salary * 0.05
        print(value1)
    else:
        value2 = salary * 0.1
        print(value2)

calculate_tax()

# task 5 (user enter everything in parameter)

def calculate_tax(age, salary, current_job):
    if age < 18 or salary < 10000 or current_job == "president":
        print("0")
    elif 10000 < salary < 20000:
        value1 = salary * 0.05
        print(value1)
    else:
        value2 = salary * 0.1
        print(value2)

calculate_tax(20, 22000, "assistant manager")


# task 6 (taking input from user)

def function_days():
    number_days = int(input("Enter how many days: "))

    years = number_days // 365
    remainder = number_days % 365
    months = remainder // 30
    remainder = remainder % 30
    days = remainder
    print(f"{years} years, {months} months and {days} days")

function_days()


# task 6 (inside the parameter)

def function_days(number_days):

    years = number_days // 365
    remainder = number_days % 365
    months = remainder // 30
    remainder = remainder % 30
    days = remainder
    print(f"{years} years, {months} months and {days} days")

function_days(4330)

# task 7 (using return)

def show_palindrome(number):
    result = ""
    for num in range(1, number):
        result += str(num)
    for num2 in range(number, 0, -1):
        result += str(num2)
    return result

print(show_palindrome(5))

# task 7 (asking from user)

def show_palindrome():
    number = int(input("Enter a number: "))
    for num in range(1, number):
        print(num, end="")
    for num2 in range(number, 0, -1):
        print(num2, end="")

show_palindrome()

# task 7 another way...

def show_palindrome(number):
    for num in range(1, number):
        print(num, end="")
    for num2 in range(number, 0, -1):
        print(num2, end="")

show_palindrome(4)



# task 8 (inside the parameter)

def show_palindromic_triangle(row):

    for item in range(1, row + 1):

        for item2 in range(1, row + 1 - item):
            print(' ', end=' ')

        for item2 in range(1, item + 1):
            print(item2, end=' ')

        for item2 in range(item - 1, 0, -1):
            print(item2, end=' ')
        print()

show_palindromic_triangle(5)

# task 8 (asking a value from user)

def show_palindromic_triangle():
    row = int(input("Enter a number: "))
    for item in range(1, row + 1):
        for item2 in range(1, row + 1 - item):
            print(' ', end=' ')
        for item2 in range(1, item + 1):
            print(item2, end=' ')
        for item2 in range(item - 1, 0, -1):
            print(item2, end=' ')
        print()

show_palindromic_triangle()


# task 9 (asking value from user)

import math

def area_circumference_generator():
    number = float(input("Enter radius of a circle: "))
    area = math.pi * number ** 2
    circumference = 2 * math.pi * number
    return area, circumference
result = area_circumference_generator()
print(result)
(tup_area, tup_circumference) = result
print(f"Area of the circle is {result[0]} and circumference is {result[1]}")
print()
result1 = area_circumference_generator()
print(result1)
(tup_area1, tup_circumference1) = result1
print(f"Area of the circle is {result1[0]} and circumference is {result1[1]}")
result2 = area_circumference_generator()
print()
print(result2)
(tup_area2, tup_circumference2) = result2
print(f"Area of the circle is {result2[0]} and circumference is {result2[1]}")


# task 9 using parameter

import math

def area_circumference_generator(number):
    area = math.pi * number ** 2
    circumference = 2 * math.pi * number
    return area, circumference

result = area_circumference_generator(1)
print(result)
(tup_area, tup_circumference) = result
print(f"Area of the circle is {result[0]} and circumference is {result[1]}")
print()
result1 = area_circumference_generator(1.5)
print(result1)
(tup_area1, tup_circumference1) = result1
print(f"Area of the circle is {result1[0]} and circumference is {result1[1]}")
result2 = area_circumference_generator(2.5)
print()
print(result2)
(tup_area2, tup_circumference2) = result2
print(f"Area of the circle is {result2[0]} and circumference is {result2[1]}")

# task 10

def make_square(num1, num2):
    dictionary = {}
    for number in range(num1, num2 + 1):
        value = number ** 2
        dictionary.update({number: value})

    return dictionary

result = make_square(5, 9)
print(result)

# task 11

def rem_duplicate(tup):
    new_list = list(tup)
    update_list = []
    for item in new_list:
        if item not in update_list:
            update_list.append(item)
    return update_list

your_list = rem_duplicate((1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6, 4, 0, 0, 0))
your_list2 = rem_duplicate(("Hi", 1, 2, 3, 3, "Hi", 'a', 'a', [1, 2]))
print(your_list)
print(your_list2)


# task 12

def function_name(elements):
    new_list = []
    for values in elements:
        if new_list.count(values) < 2:
            new_list.append(values)
    return new_list

element = [1, 2, 3, 3, 3, 3, 4, 5, 8, 8]
removed_list = function_name(element)
print(f"Removed: {len(element) - len(removed_list)}\n{removed_list}")

element2 = [10, 10, 15, 15, 20]
removed_list2 = function_name(element2)
print(f"Removed: {len(element2) - len(removed_list2)}\n{removed_list2}")



# task 13

operator = str(input("Enter a operator: "))
first_value = float(input("Enter a number: "))
second_value = float(input("Enter a number: "))

def basic_calculator():
    if operator == "+":
        return first_value + second_value
    elif operator == "-":
        return first_value - second_value
    elif operator == "/":
        return first_value / second_value
    elif operator == "*":
        return first_value * second_value
    else:
        return "invalid"

result = basic_calculator()
print(result)

task 14

limit = int(input("Sir, please enter your range: "))
list_1 = []

for item in range(0, limit):
    item_name = input("Sir, please sir enter your item name: ").lower()
    list_1.append(item_name)

dictionary = {'rice': 105, 'potato': 20, 'chicken': 250, 'beef': 510, 'oil': 85}

def function_name(list_1, location='Dhanmondi'):
    sum1 = 0

    for item2 in range(0, list_1):
        sum1 = sum1 + dictionary[list_1[item2]]

    print('Sir, your bill is', sum1)

    if location == "Dhanmondi":
        sum1 += 30
    else:
        sum1 += 70
    print('Sir, your bill is', sum1)

function_name(list_1)

user = "Rice, oil, beef"
result = user.lower()
list_1 = result.split(", ")
print(list_1)


def function_name(sentence, position):
    taken = ""
    out = ""
    for char in range(len(sentence)):
        if char % position != 0 or char == 0:
            taken += sentence[char]
        else:
            out += sentence[char]

    return taken + out

sentence = input("Enter your sentence: ")
position = int(input("Enter your position: "))

result = (taken + out)
print()

"""