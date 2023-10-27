def say_my_name():
    print("Hey, I am Brian")

say_my_name()
say_my_name()

def say_my_name(name = "User"):
    print(f"Hey, I am { name }")

say_my_name("Kavete")
say_my_name()

def calculate_volume_cylinder(radius, height):
    volume = 22/7 * radius**2 * height
    return volume

print(calculate_volume_cylinder(4, 56))

print(calculate_volume_cylinder(7, 30))

volume1 = calculate_volume_cylinder(15, 50)

print(round(volume1))

def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_numbers(6, 87, 45, 655, 34))

# Named parameters

print(calculate_volume_cylinder(height=45, radius=5))
