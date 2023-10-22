my_tuple = ("Jujutsu", "Naruto", "One Piece", "Bleach")

print(my_tuple[0])

# A tuple with a single value should be followed by a ,
tuple_two = ("Dragon Ball",)

if "Naruto" in my_tuple:
    print("Dattebayo")

# Changing value in a tuple
my_list = list(my_tuple)
my_list[2] = "Kengan"
my_tuple = tuple(my_list)

print(my_tuple)

my_tuple += tuple_two
print(my_tuple)
print(tuple_two)
del tuple_two


# Unpacking a tuple
(anime1, anime2, anime3, anime4, anime5) = my_tuple
print(anime3)


(x, *y, z) = my_tuple

# y will be a list
print(y) 

for x in my_tuple:
    print(x)

for i in range(len(my_tuple)):
    print(my_tuple[i])

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1

# return index of a  value 
y = my_tuple.index("Bleach")
print(y)

tuple2 = tuple(("Demon Slayer", "Attack on Titan"))
newtuple = my_tuple + tuple2;

print(newtuple)

# Number of times "Bleach" occurs in the tuple
print(newtuple.count("Bleach"))

print(newtuple.index("Naruto"))
