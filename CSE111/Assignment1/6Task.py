empty_list = []

list1 = []
count = 0

while True:

    var = input()

    if var == "STOP":
        break
    else:
        empty_list.append(int(var))

for item in empty_list:
    if item not in list1:
        list1.append(item)
for item2 in list1:
    count = 0
    for i in empty_list:
        if item2 == i:
            count = count + 1

    print(item2, "-", count, "times")