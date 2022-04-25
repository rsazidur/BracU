'''

# using insert

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.insert(2, 'bajaj')
print(motorcycles)
motorcycles.insert(2, 'walton')
print(motorcycles)

# appending element in a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
motorcycles.append('bajaj')
print(motorcycles)

# modifying elements in a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[0] = 'bajaj'
print(motorcycles)
motorcycles[2] = 'walton'
print(motorcycles)


# using del

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

# using pop
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles_popped = motorcycles.pop()
print(motorcycles)
print(motorcycles_popped)



# removing item by value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)



# Try yourself task

# guest_name = str(input("Enter your guest name that you're going to invite: ").split(","))
# print(guest_name)

guest_name = ['sazid', 'avisekh', 'fahad', 'trisha']
print(guest_name)
print()
print(f"{guest_name[0]} that's me")
print(f"{guest_name[1]} a good guy i guess, helpful and friendly.")
print(f"{guest_name[2]} he is my university life first friend.")
print(f"{guest_name[3]} please, wear a sari, you look beautiful in that.")
print()
friend1 = guest_name.pop(1)
friend2 = guest_name.pop(1)

print(f"{friend1} and {friend2} are busy at study that's why they didn't come.")

print(guest_name)
print()
guest_name.append('saad')
guest_name.append('mugdho')
print(guest_name)
print(f"{guest_name[0].title()} that's me")
print(f"{guest_name[3].title()} helpful and friendly, he got 4 course in 1st semester.")
print(f"{guest_name[2].title()} he is my friend, multi-talented but idk he look like broken.")
print(f"{guest_name[1].title()} please, wear a sari, you look beautiful in that.")
print()
print(guest_name)

print()
guest_name.insert(0, 'rafi')
guest_name.insert(3, 'ome')
guest_name.insert(6, 'fardin')
print(guest_name)
print()
print(f"{guest_name[1].title()} that's me")
print(f"{guest_name[5].title()} helpful and friendly, he got 4 course in 1st semester.")
print(f"{guest_name[4].title()} he is my friend, multi-talented but idk he look like broken.")
print(f"{guest_name[2].title()} please, wear a sari, you look beautiful in that.")
print(f"{guest_name[6].title()} he is collage friend and he is jem.")
print(f"{guest_name[3].title()} he is collage friend and he is jem.")
print(f"{guest_name[0].title()} he is collage friend and he is jem.")
print()
print()
print("Sorry, i can invite only two person.")
print()
new_guest_name = guest_name.pop(0)
print(f"{new_guest_name} I am sorry.")
new_guest_name = guest_name.pop(2)
print(f"{new_guest_name} I am sorry.")
new_guest_name = guest_name.pop(3)
print(f"{new_guest_name} I am sorry.")
new_guest_name = guest_name.pop(2)
print(f"{new_guest_name} I am sorry.")
new_guest_name = guest_name.pop(2)
print(f"{new_guest_name} I am sorry.")
print()
print(guest_name)

del guest_name[0]
del guest_name[0]
print(guest_name)

'''

