operation = input("Set Operation (1=Union, 2=Intersection, 3=Complement, 4=Difference, 5=Cross Product):")

string1 = [int(i) for i in input("A: ").split()]
string2 = [int(i2) for i2 in input("B: ").split()]

if operation == "1":
    empty_list_1 = []
    empty_list_2 = []
    for item in string1:
        if item not in empty_list_1:
            empty_list_1.append(item)
    for item in string2:
        if item not in empty_list_2:
            empty_list_2.append(item)
    empty_list_1.extend(empty_list_2)
    final_list = []
    for item in empty_list_1:
        if item not in final_list:
            final_list.append(item)
    print("A U B: ", sorted(final_list))
    
elif operation == "2":
    empty_list_1 = []
    empty_list_2 = []
    for item in string1:
        if item not in empty_list_1:
            empty_list_1.append(item)
    for item in string2:
        if item in empty_list_2:
            empty_list_2.append(item)
    empty_list_1.extend(empty_list_2)
    final_list = []
    for item in empty_list_1:
        if item not in final_list:
            final_list.append(item)
    print("A ∩ B: ", sorted(final_list))
    
elif operation == "3":
    pass
    


    
