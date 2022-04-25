# CSE110 Assignment 2 (Loops)
"""
# task 1 (a)

for item in range(24, -12, -6):
    if item == -6:
        print(-6)
    else:
        print(item, end=', ')

# (b)

for item in range(-10, 25, 5):
    if item == 20:
        print(20)
    else:
        print(item, end=', ')



# (c)

for item in range(18, 72, 9):
    if item == 63:
        print(63)
    else:
        print(item, end=', ')


# (d)

for item in range(18, 72, 9):
    if item % 2 == 0:
        print(item, end=', ')

    elif item == 63:
        print(item * -1, end=' ')

    else:
        print(item * -1, end=', ')


# task 2

name = input('Enter your favorite car name: ')
num = int(input('Enter a number: '))

for item in range(num):
    print(name)

# task 3

sum1 = 0
for item in range(1, 601):
    if item % 7 == 0 and item % 9 == 0:
        sum1 = sum1 + item
        if item == 567:
            print(567, end=' = ')
        else:
            print(item, end=' + ')
print(sum1, sep='')


# task 4

sum1 = 0
for item in range(1, 601):
    if item % 7 == 0 or item % 9 == 0:
        sum1 = sum1 + item
print(sum1)


# task 5

sum1 = 0
for item in range(1, 601):
    if item % 7 == 0 or item % 9 == 0:
        if item % 7 != item % 9:
            sum1 = sum1 + item
print(sum1)


# task 6

for item in range(10, 51):
    if item % 2 != 0:
        print(item, end=' ')



# task 7

sum1 = 0
sum2 = 0
value = int(input('Enter a number for the expression: '))

for item in range(1, value + 1):
    if item % 2 == 0:
        new_value1 = (item * item) * - 1
        print(new_value1, end=' ')
        sum1 = sum1 + new_value1
    else:
        new_value2 = (item * item)
        print(new_value2, end=' ')
        sum2 = sum2 + new_value2
print()
print(sum1 + sum2)




# way 2

sum1 = 0
value = int(input('Enter a number for the expression: '))

for item in range(1, value + 1):
    if item % 2 == 0:
        sum1 = sum1 - (item * item)
    else:
        sum1 = sum1 + (item * item)

print(sum1)



# task 8

sum1 = 0
count = 0
for item in range(1, 11):
    num = int(input('>>> '))

    if num % 2 != 0:
        sum1 = sum1 + num
        count = count + 1
average = sum1 / count

print('Sum is :', sum1)
print('Average is :', average)



# task 9

sum1 = 0
num = int(input('Enter any number: '))

for item in range(1, num + 1):
    if item % 7 == 0:
        sum1 = sum1 + item

print(sum1)


# task 10

sum1 = 0
for item in range(1, 6):
    num = int(input('>>> '))
    sum1 = sum1 + num
    print(sum1)



# task 11

num = int(input('Enter any number: '))


for number in range(num):
    if 0 < num:
        remainder = num % 10
        if num < 10:
            print(remainder)
        else:

            print(remainder, end=', ')
        num = num // 10



# task 12

num = int(input('Enter any number: '))

count = 0
for item in range(num):
    if 0 < num:
        num = num // 10
        count += 1
print(count)



# task 13

num = int(input('Enter any number: '))
count = 0
r_comma = ''

for item in range(1, num + 1):
    if num % item == 0:
        r_comma += str(item) + ', '
        count += 1
print(r_comma[0:len(r_comma) - 2])

print(count)


# task 15

num = int(input('Enter any number: '))

sum1 = 0
for item in range(1, num):
    if num % item == 0:
        sum1 += item
if sum1 == num:
    print(num, 'is a perfect number.')
else:
    print(num, 'not a perfect number.')



# task 16

num = int(input('Enter any number: '))

count = 0
if num == 0 or num == 1:
    print('Not a prime number.')
else:
    for item in range(2, num):
        if num % item == 0:
            count += 1
        break
    if count == 0:
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')

# way 2

num = int(input('Enter any number: '))

count = 0
for item in range(1, num + 1):
    if num % item == 0:
        count += 1
if count == 2:
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')



quantity = int(input('Enter how many number you want: '))

sum1 = 0
maximum = 0
minimum = 0
for item in range(1, quantity + 1):
    num = int(input('>>> '))
    sum1 = sum1 + num

    if num > maximum:
        maximum = num
    elif num < minimum:
        minimum = num

average = sum1 / 5
print(sum1, 'and', average)
print('Maximum =', maximum, 'and Minimum =', minimum)


# task 18

num = int(input('Enter any number: '))

for item in range(1, num + 1):
    print('+' * num)


# task 19

num1 = int(input('Enter any number: '))
num2 = int(input('Enter any number: '))

for row in range(1, num1 + 1):
    for column in range(1, num2 + 1):
        print(column, end='')
    print()



# task 20

num1 = int(input('Enter any number: '))

for row in range(1, num1 + 1):
    for column in range(1, row + 1):
        print(column, end='')
    print()

# task 21

num = int(input('How many fibonacci series you want: '))

i = 0
first_num = 0
second_num = 1

if 0 > num:
    print('Please enter positive number.')
else:
    while i <= num:
        if i <= 1:
            Next = i

        else:
            Next = first_num + second_num
            first_num = second_num
            second_num = Next
        print(Next, end=' ')
        i += 1



# task 22

num = int(input('>>: '))

binary = 0
i = 0
while num != 0:
    remainder = num % 2
    quantity = 10 ** i
    binary = remainder * quantity + binary
    num = num // 2
    i += 1
print(binary)


# task 23

num = int(input('Enter a binary number: '))

i = 0
decimal = 0
while num != 0:
    remainder = num % 10
    quantity = 2 ** i
    decimal = remainder * quantity + decimal
    num = num // 10
    i += 1
print(decimal)



# task 24

f_num = int(input('Enter your first number: '))
s_num = int(input('Enter your second number: '))

prime_count = 0
perfect_count = 0

for num in range(f_num, s_num + 1):
    count = 0
    for item in range(1, num):
        if num % item == 0:
            count += 1
    if count == 2:
        print('prime')
    else:
        print('not prime')
    prime_count += 1
    print(prime_count)

sum1 = 0
for item in range(1, s_num):
    if s_num % item == 0:
        sum1 += item
if s_num == sum1:
    print('Perfect')
else:
    print('not perfect')

    perfect_count += 1
    print(perfect_count)




# task 25

f_num = int(input('Enter first number: '))
s_num = int(input('Enter second number: '))
t_num = int(input('Enter a number to divisible: '))



# Extra task 1

num = int(input('Enter a number between (1-9): '))

i = 0
p = 1
if 1 < num < 10:
    while i < num:
        i += 1
        print(i, end='')
    while num > p:
        num -= 1
        print(num, end='')

else:
    print('Invalid number.')



num = int(input('Enter a number between (1-9): '))

if 1 < num < 10:
    for item in range(1, num + 1):
        print(item, end='')
    for item in range(num - 1, 0, -1):
        print(item, end='')
else:
    print('Invalid number.')

# task 2

num = int(input('Enter a number: '))

first_n = 0
second_n = 1
for i in range(num):
    if i <= 1:
        Next = i
    else:
        Next = first_n + second_n
        first_n = second_n
        second_n = Next
    print(Next, end=' ')



# task 3

num = int(input('Enter any number: '))

sum1 = 0
for item in range(1, num + 1):
    new_number = (item ** item) // item
    sum1 = sum1 + new_number
print(sum1)

# task 4

lower_year = int(input('Enter any lower bound year: '))
upper_year = int(input('Enter any upper bound year: '))

for year in range(lower_year, upper_year + 1):

    if year % 4 == 0 and year % 100 != 0:
        print(year, end=' ')

    elif year % 100 == 0 and year % 400 == 0:
        print(year, end=' ')



# task 5

sum1 = 0
i = 0
while True:
    num = int(input('>>. '))
    if num == 'stop':
        break
    else:
        sum1 = num * num
    i += 1
print(sum1)

"""