this_dict = {
    "name": "Brian",
    "university": "Moi",
    "school": "engineering",
    "year": 4
}
print(this_dict["university"])

another_dict = {
    "name": "Kavete",
    "university": "Jkuat",
    "school": "Science",
    "year": 3
}

my_dict = dict(name="Naruto", main="Dattebayo")

print(my_dict)

print(this_dict.get("school"))

x = this_dict.keys()

print(x)

print(type(x))

y = this_dict.values()

print(y)

z = this_dict.items()

print(z)
print(type(z))

if "name" in this_dict:
    print("You have a name")

# Change value
my_dict["name"] = "One Piece"

# Update value
my_dict.update({"main": "Luffy"})
print(my_dict)

my_dict["girl"] = "Nami"

my_dict.update({"cyborg": "Franky"})

print(my_dict)

this_dict.pop("year")
print(this_dict)

# Remove last added item
another_dict.popitem()

print(another_dict)

del my_dict["girl"]
print(my_dict)
# print keys
for x in this_dict:
    print(x)
# Print values
for x in this_dict.values():
    print(x)
# or
for x in my_dict:
    print(my_dict[x])

# Both keys and values
for x, y in another_dict.items():
    print(x, y)

new_dict = another_dict.copy()
print(new_dict)

new_dict = dict(my_dict)
print(new_dict)

# Nested Dictionaries

anime = {
    "anime1": {
      "name": "Bleach",
      "main": "Ichigo"
    },
    "anime2": {
        "name": "Dragon Ball",
        "main": "Goku"
    },
    "anime3": {
        "name": "Jujutsu Kaisen",
        "main": "Unknown"
    }
}
print(anime)
print(anime["anime2"]["name"])
