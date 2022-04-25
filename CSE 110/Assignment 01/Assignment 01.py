"""
# CSE Lab 01 task 01

f_num = int(input('Enter first number: '))
s_num = int(input('Enter second number: '))

sum1 = f_num + s_num

product = f_num * s_num

difference = f_num - s_num

print('Sum = ', sum1, '\nProduct =', product, '\nDifference = ', difference)



# Task 2

import math

radius = float(input('Enter the radius of a circle: '))

area = math.pi * radius * radius

circumference = 2 * math.pi * radius

print('Area is :', area)
print('Circumference is :', circumference)


# Task 03

f_num = int(input('Enter the first number: '))
s_num = int(input('Enter the second number: '))

if f_num == s_num:
    print('The numbers are equal.')
elif f_num > s_num:
    print('First number is greater.')
else:
    print('Second number is greater.')



# task 4

f_num = int(input('Enter the first number: '))
s_num = int(input('Enter the second number: '))

if f_num > s_num:
    num1 = f_num - s_num
    print(num1)
else:
    num2 = s_num - f_num

    print(num2)


# task 5

num = int(input('Enter your number: '))

if num % 2 == 0:
    print('Number is even.')
else:
    print('Number is odd.')

# task 6

num = int(input('Enter the number: '))

if num % 2 == 0 or num % 5 == 0:
    print(num)
else:
    print('Not a multiple of 2 OR 5')

# task 7

num = int(input('Enter any number: '))

# num % 2 != 0 and num % 5 == 0 or num % 2 == 0 and num % 5 != 0:
if num % 2 == 0 or num % 5 == 0:
    if num % 2 != num % 5:
        print(num)
    elif num % 2 == 0 and num % 5 == 0:
        print('Multiple of 2 and 5 both.')
    else:
        print('Not a multiple we want.')


# task 8

num = int(input('Enter any number: '))

if num % 2 == 0 and num % 5 == 0:
    print(num)
else:
    print('Not multiple of 2 and 5 both')


# task 9

num = int(input('Enter given number of seconds: '))

hour = num // 3600
remain = num % 3600
minutes = remain // 60
remain = remain % 60
second = remain


print('Hours:', hour, 'Minutes:', minutes, 'Second:', second)



# task 10

time = int(input('Enter the hours you have worked: '))

if 0 <= time:
    if time <= 40:
        salary1 = time * 200
        print(salary1)
    elif time <= 168:
        salary2 = ((time - 40) * 300) + 8000
        print(salary2)
    else:
        print('Cant work more than 168 hours in weekly.')

else:
    print('Enter valid hour.')


# task 11

num = int(input('Enter a number(S) to know the value of L: '))

if num < 100:
    value1 = 3000 - 125 * (num ** 2)
    print(value1)

else:
    value2 = 12000 / (4 + (num ** 2) / 14900)
    print(value2)



# task 12

time = int(input('What is the time right now?: '))

if 0 <= time < 24:

    if 4 <= time <= 6:
        print('Breakfast.')
    elif 12 <= time <= 13:
        print('Lunch.')
    elif 16 <= time <= 17:
        print('Snacks.')
    elif 19 <= time <= 20:
        print('Dinner>')
    else:
        print('Patience is a virtue')
else:
    print('Wrong time.')


# task 13

mark = int(input('Enter your mark: '))

if 0 <= mark <= 100:

    if mark >= 90:
        print('A')
    elif mark >= 80:
        print('B')
    elif mark >= 70:
        print('C')
    elif mark >= 60:
        print('D')
    elif mark >= 50:
        print('E')
    else:
        print('F')
else:
    print('Invalid mark.')

# task 15

temp = int(input('Enter the temperature: '))
con_temp = int((temp - 32) * 0.56)

if con_temp < 19:
    print(con_temp, 'C', 'Winter.')

elif 20 <= con_temp <= 24:
    print(con_temp, 'C', 'Autumn')

elif 25 <= con_temp <= 29:
    print(con_temp, 'C', 'Spring')

else:
    print(con_temp, 'C', 'Summer.')


# task 16

dist = int(input('Enter the distance: '))
time = int(input('Enter the time: '))

con_dist = dist / 1000
con_time = time / 3600
value = float("{0:.2f}".format(con_dist / con_time))

# value = (dist/1000) / (time / 3600)

if value < 60:
    print(value, 'Km/h', '\nToo slow. Needs more changes.')

elif 60 <= value <= 90:
    print(value, 'Km/h', '\nVelocity is okay. The car is ready!')

else:
    print(value, 'Km/h', '\nToo fast. Only a few changes should suffice.')



# task 16

cgpa = float(input('Enter your Cgpa: '))
credit = int(input('Enter your credits: '))

if cgpa >= 3.80 and credit >= 30:
    if 3.80 <= cgpa <= 3.89:
        print('The student is eligible for a waiver of 25 percent.')
    elif 3.90 <= cgpa <= 3.94:
        print('The student is eligible for a waiver of 50 percent.')
    elif 3.95 <= cgpa <= 3.99:
        print('The student is eligible for a waiver of 75 percent.')
    elif cgpa == 4.00:
        print('The student is eligible for a waiver of 100 percent.')
    else:
        print('Give a valid cgpa.')

else:
    print('The students is not eligible for a waiver')



# task 17 and 18 are similar

# task 19

canvas = int(input('Enter how many canvas she order: '))
tube = int(input('Enter how many canvas she order: '))

total = (canvas * 120) + (tube * 75)

if 0 <= total < 300:
    print('Total:', total, '\nNo discount.')

elif 300 <= total < 500:
    print('Total:', total, '\nAfter discount:', total - 10)

elif 500 <= total < 750:
    print('Total:', total, '\nAfter discount:', total - 20)

elif 750 <= total < 1000:
    print('Total:', total, '\nAfter discount:', total - 50)

else:
    print('Total:', total, '\nAfter discount:', total - 150)



# Special task 4

year = int(input('Enter a year to know leap or not: '))

if year % 400 == 0 and year % 100 == 0:
    print(year, 'Year is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print(year, 'Year is a leap year')
else:
    print('Not a leap year.')



# task 3
import math

x = int(input('Enter the value of X: '))
y = int(input('Enter the value of Y: '))
z = int(input('Enter the value of Z: '))

s = (x + y + z) / 2

area = s * math.sqrt((s - x) * (s - y) * (s - z))

print(area)



# task 2

x = int(input('Enter the value of an angel: '))
y = int(input('Enter the value of an angel: '))
z = int(input('Enter the value of an angle: '))

if condition:
    print('Valid triangle.')
else:
    print('Not a valid triangle.')



# task 1

money = int(input('Enter how much money: '))

five_hun = money // 500
remain = money % 500
two_hun = remain // 200
remain = remain % 200
one_hun = remain // 100
remain = remain % 100
fifty = remain // 50
remain = remain % 50
twenty = remain // 20
remain = remain % 20
ten = remain // 10
remain = remain % 10
five = remain // 5
remain = remain % 5
two = remain // 2
remain = remain % 2
one = remain // 1
remain = one

print("500 Taka:", five_hun, 'Notes',
      '\n200 Taka:', two_hun, 'Notes',
      '\n100 Taka', one_hun, 'Notes',
      '\n50 Taka:', fifty, 'Notes',
      '\n20 Taka:', twenty, 'Notes',
      '\n10 Taka:', ten, 'Notes',
      '\n5 Taka:', five, 'Notes',
      '\n2 Taka:', two, 'Notes',
      '\n1 Taka:', one, 'Notes',)
"""