this_set = {"HTML", "CSS", "JS", "jQuery"}
set2 = {"Bootstrap", "Django", "Python"}

print(type(set2))

for x in this_set:
    print(x)
if "JS" in this_set:
    print("Learn ReactJs")

this_set.add("ReactJS")
print(this_set)

this_set.update(set2)
print(this_set)

# Raises an error if value not found
this_set.remove("jQuery")

print(this_set)
# Does not raise and error if value not found
this_set.discard("Tailwind")
print(this_set)

# Remove random item
x = this_set.pop()
print(x)

set2.add("SQL")

print(set2)
new_set = this_set.union(set2)
print(new_set)

set3 = {"JavaScript", "HTML", "CSS3", "React", "Python3", "Django", "Bootstrap"}

z = set3.intersection(new_set)

print(z)

y = set3.symmetric_difference(new_set)

print(y)

set3.symmetric_difference_update(new_set)

print(set3)

set4 = this_set.copy()

print(set4)