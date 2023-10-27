import json

json_data = '{"name": "Brian", "age": 21, "city": "Nairobi", "hails": "Kalongo", "height": 1.87 }'

py_dict = json.loads(json_data)

print(py_dict)

some_dict = {
    "name": "One Piece",
    "main": "Luffy",
    "mangaka": "Oda",
    "year": 1998,
    "episodes": 1085
    }


from_dict = json.dumps(some_dict)

print(from_dict)
print(some_dict)

print(type(some_dict))

print(type(from_dict))

my_list = ["One Piece", "Naruto", "Bleach", "Kengan Ashura", "Dragon Ball"]

list_json = json.dumps(my_list)
print(list_json)
print(type(list_json))

print(json.dumps(True))
print(json.dumps(None))


indented = json.dumps(some_dict, indent=4)

print(indented)

separated = json.dumps(some_dict, indent=4, separators=(", ", "= "), sort_keys=True)

print(separated)
