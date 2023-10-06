# declare my list, print it and check type
my_list = ["Lamborghini", "Audi", "Jeep", "Maserati", "Aston Martin"]
print(my_list)
print(type(my_list))

# change a value
my_list[0] = "BMW"
print(my_list)

# display a value at an index
print(my_list[2])

# remove a value from the list
my_list.remove("Jeep")
print(my_list)

# Remove a value at an index
my_list.pop(3)
print(my_list)

# add a value to the end of the list
my_list.append("Lexus")
print(my_list)

# insert a value at an index
my_list.insert(3, "Mazda")
print(my_list)

# create new list and extend my_list
# extend can also be used with other collections such as tuples
toyota = ["prado", "probox", "passo", "premio", "harrier"]
my_list.extend(toyota)
print(my_list)

# Replace a range of values
toyota[1:3] = ["landCruiser", "hilux"]
print(toyota)

# Also deletes a value at an index
del my_list[0]
print(my_list)

# Loop through my_list
for x in my_list:
    print(x)

# loop through toyota
i = 0
for i in range(len(toyota)):
    print(toyota[i])