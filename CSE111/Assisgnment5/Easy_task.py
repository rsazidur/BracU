operation = input("Set Operation (1=Union, 2=Intersection, 3=Complement, 4=Difference, 5=Cross Product):")



if operation == "1":
    
    string1 = [int(i) for i in input("A: ").split()]
    string2 = [int(i2) for i2 in input("B: ").split()]
    
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
    
    string1 = [int(i) for i in input("A: ").split()]
    string2 = [int(i2) for i2 in input("B: ").split()]
    
    string1_as_set = set(string1)
    intersection = string1_as_set.intersection(string2)
    intersection_as_list = list(intersection)

    print(intersection_as_list)   
    
elif operation == "3":
    
    string1 = [int(i) for i in input("A: ").split()]
    string2 = [int(i2) for i2 in input("Universal Set, U: ").split()]
    
    if string2 not in string1:
        empty_list_1 = []
        empty_list_2 = []
        for item in string1:
            if item not in empty_list_1:
                empty_list_1.append(item)
        for item in string2:
            if item not in empty_list_2:
                empty_list_2.append(item)
        empty_list_1.pop(empty_list_2)
        print(empty_list_1)
    else:
        print("Error: First Set Containing Elements that are not a Part of the Universal Set.")
        
elif operation == "4":
    
    string1 = [int(i) for i in input("A: ").split()]
    string2 = [int(i2) for i2 in input("B: ").split()]

    new_string = string1 - string2
    
    print("A - B: ", new_string)