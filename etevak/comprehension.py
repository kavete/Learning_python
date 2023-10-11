brands = ["Honda", "Toyota", "Subaru", "Nissan", "Isuzu", "Mazda"]
cars = list(("Harrier", "X-trail", "D-max", "Rav4", "Impreza", "Land cruiser"))

[print(x) for x in brands]

# Make a new list containing only the values with "e"
cars_list = [x for x in cars if "e" in x]

print(cars_list)

brands_lower =[x.lower() for x in brands]

print(brands_lower)

cars_upper = [x.upper() for x in cars]

print(cars_upper)
