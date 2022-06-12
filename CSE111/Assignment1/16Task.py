def foodpanda(food, location="Mohakhali"):
    if location != "Mohakhali":
        delivery_charge = 60
    else:
        delivery_charge = 40

    if food == "BBQ Chicken Chess Burger":
        meal_cost = 250
    elif food == "Beef Burger":
        meal_cost = 170
    elif food == "Naga Drums":
        meal_cost = 200
    else:
        return "The food is not on the Menu."

    tax = meal_cost * (8 / 100)

    Total_Price = meal_cost + delivery_charge + tax
    return Total_Price


food = input()
location = input()

if location != "":
    print(foodpanda(food, location))
else:
    print(foodpanda(food))

