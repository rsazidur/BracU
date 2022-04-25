"""
def summation():
    first = int(input("Enter your first number: "))
    second = int(input("Enter your second number: "))
    print(first + second)
summation()

def summation(first, second):
    print(first + second)
summation(45, 67)


def summation():
    first = int(input("Enter your first number: "))
    second = int(input("Enter your second number: "))
    third = int(input("Enter your third number: "))
    print(first + second + third)
summation()


def summation(*value):
    for item in value:
        print(item + item)
summation(45, 67, 76, 87)


def summation(value, *values):
    print(value)
    print(values)
summation(45, 67, 76, 87)


# key arguments (key,  value) passing the key along with values
def sparda_child(child3, child2, child1):
    print("The Twin child is,", child3)

sparda_child(child1="Dante", child2="Vergil", child3="Dante and Vergil"


# argument as a dictionary
def dante_sword(**dante):
    print("Sword is", dante["name"])
dante_sword(name="Rebellion", trademark="magic sword")


#  passing the key along with values
def dante_sword(**dante):
    print("Item is", dante["power"])
dante_sword(name="Rebellion", trademark="magic sword", gun="Ebony & Ivory", power="Supernatural Strength")


# default key argument.

def dante_fighting(x, y=5):
    return x * x + 2 * x * y + y * y
print("If Dante go North way:", dante_fighting(2))
print("If Dante go East way:", dante_fighting(2, 10))



# return statement (fruitful function) return a value

def dante_multi(x):
    return x * 5
# print(dante_multi(4), end=" ")
# print(dante_multi(5), end=" ")
# print(dante_multi(6))

print("If dante take red orb, point is", dante_multi(6))
print("If dante take green orb, point is", dante_multi(4))
print("If dante take blue orb, point is", dante_multi(10))



# Example why we use function.
# sort? what is sort ?
# here is two given list bellow:

list_1 = [46, 45, 56, 23, 73, 60]
list_2 = [89, 45, 5, 34, 23, 16, 20]

# sort the list without using sort function.
for item in range(len(list_1)):
    for item2 in range(item + 1, len(list_1)):

        if list_1[item] > list_1[item2]:
            temp = list_1[item]
            list_1[item] = list_1[item2]
            list_1[item2] = temp

print(list_1)

for item in range(len(list_2)):
    for item2 in range(item + 1, len(list_2)):

        if list_2[item] > list_2[item2]:
            temp = list_2[item]
            list_2[item] = list_2[item2]
            list_2[item2] = temp

print(list_2)


# what if they give us more list to sort... in that case we use function.

def sort_list(Numlist):
    for item in range(len(Numlist)):
        for item2 in range(item + 1, len(Numlist)):

            if Numlist[item] > Numlist[item2]:
                temp = Numlist[item]
                Numlist[item] = Numlist[item2]
                Numlist[item2] = temp

    print(Numlist)

list_1 = [46, 45, 56, 23, 73, 60]
list_2 = [89, 45, 5, 34, 23, 16, 20]

sort_list(list_1)
sort_list(list_2)

"""
