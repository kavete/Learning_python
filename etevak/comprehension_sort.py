brands = ["Honda", "Toyota", "Subaru", "Nissan", "Isuzu", "Mazda"]
cars = list(("Harrier", "X-trail", "D-max", "Rav4", "Impreza", "Land cruiser"))

[print(x) for x in brands]

# Make a new list containing only the values with "e"
cars_list = [x for x in cars if "e" in x]

print(cars_list)

brands_lower = [x.lower() for x in brands]

print(brands_lower)

cars_upper = [x.upper() for x in cars]

print(cars_upper)

#  Sorting
cars_upper.sort()
print(cars_upper)

brands.sort(reverse=True)
print(brands)

numbers = [156, 67, 165, 23, 98, 76, 45, 78]


def hundred(n):
    return abs(n - 100)


numbers.sort(key=hundred)
# Sorts the numbers according to how close to 100 they are
print(numbers)

brands.sort(key=str.lower)
print(brands)

new_cars = cars.copy()
cars.append("Wish")
print(new_cars)

