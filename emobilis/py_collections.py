cities = ["Brazzaville", "Djibouti", "Kampala", "Lagos", "Cape Town", "Addis Ababba", "Cairo"]

scores = [56, 67, 76, 36, 90, 78, 59]

car = {
    "brand": "Toyota",
    "model": "Harrier",
    "color": "black",
    "year": 2020,
    "gear": "Manual",
    "owners": ["Etevak", "Brian", "Mwendwa"]
}

friends = {"Jack", "Fidel", "Fred", "Ken", "John", "John"}  # unique elements and unordered

print(friends)

workers = ("Jack", "Stan", "Etevak")  # *immutable

print(friends)
print(workers)
print(car)

print(cities[1])

print(cities[-1])  # last element

print(car["model"])

print(f"The car's color is {car['color']}")

# loop

for city in cities:  # for each city in cities
    print(city)

for key, value in car.items():
    print(key, value)

for key in car:
    print(key)
for values in car.values():
    print(values)
for key in car.keys():
    print(key)
