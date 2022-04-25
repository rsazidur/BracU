"""
# Task 1 Write a Python program that takes a String as an input from the user and prints that String in reverse order.

number = input("Enter anything to reverse: ")
reversed_string = ''
index = len(number)
while index > 0:
    reversed_string += number[index - 1]
    index = index - 1
print(reversed_string)


# using for loop

number = input("Enter anything for reverse: ")
for item in range(len(number)-1, -1, -1):
    print(number[item], end='')



# Task 2

first_str = input("Enter the first String: ")
second_num = int(input("Enter the second number: "))
if len(first_str) > 1:
    for item in range(second_num, -1, -1):
        print(first_str[item], end='')
    print(first_str[second_num + 1:len(first_str): 1])
else:
    print("Please enter a string that is greater than 1")



# Task 3

string_input = input('Enter Anything: ')
check = '01'
count = 0

for char in string_input:

    if char not in check:
        count += 1
        break
    else:
        pass

if count == 0:
    print('Binary Number')
else:
    print('Not a Binary Number')


# task 4

word = input("Enter any word: ")
length = len(word)

if word.endswith('est'):
    print(word)

elif word.endswith('er'):
    print(word[0:length - 2] + 'est')

elif length > 3:
    print(word + 'er')

elif length < 4:
    print(word)

# Task 5

word = input('Enter any word: ')
for outside in range(0, len(word)):
    for inside in range(0, outside + 1):
        print(word[inside], end='')
    print()



# task 6

word = input('Enter any word: ')
for item in range(0, len(word)):
    print(word[item], ':', ord(word[item]))



# test 7

word = input('Enter any word: ')
lower_word = word.lower()
next1 = 0
for item in range(0, len(lower_word)):
    if lower_word[item] == 'z':
        print('a', end='')
    else:
        next1 = ord(lower_word[item]) + 1
        print(chr(next1), end='')





# task 8

word = input('Enter any word: ')
result = ''
for item in range(len(word)):
    if item % 2 != 0:
        result = result + word[item]

i = 0
upper_char = ''

while len(result) > i:
    if 'a' <= result[i] <= 'z':
        upper_char += chr(ord(result[i]) - 32)
    else:
        upper_char += chr(ord(result[i]))
    i += 1
print(upper_char)


# task 9

word = input('Enter any word: ')
sep = input()
add = ''
for item in range(0, len(word)):
    if sep == word[item]:
        print(add)
        add = ''
    else:
        add = add + word[item]

# task 10

word = input('Enter anything: ')
new_word = word[0]

for item in word:
    if item == new_word[- 1]:
        continue

    else:
        new_word = new_word + item

print(new_word)

# task  11

word = input('Enter any word: ')
letter = input('Enter a letter: ')

if len(word) < 3:
    print(word)

elif letter in word:
    print(word.replace(letter, ''))

else:
    print(word[1:len(word) - 1])


# task 12

user = input('Enter two string with a comma and space: ')
find = user.find(', ')
first_string = user[0:find]
second_string = user[find + 2:]


if len(first_string) > len(second_string):
    small = len(second_string)

    for item in range(0, small):
        print(first_string[item] + second_string[item], end='')
    print(first_string[small:])

else:
    var = len(first_string) < len(second_string)
    small = len(first_string)

    for item in range(0, small):
        print(first_string[item] + second_string[item], end='')
    print(second_string[small:])

"""