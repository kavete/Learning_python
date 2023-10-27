name = "Etevak"
city = "NewYork"
age = 35
weight = 70


print(name + city)
print(name * 4)

print(f"My name is { name }, I am { age } years old, I weigh { weight } kgs and I live in { city }")
sentence = "These are python string methods"

uppercase = sentence.upper()
print(uppercase)
print(sentence)

print(sentence.lower())

number_of_chars = len(sentence)

print(number_of_chars)

print(sentence.swapcase())

print(sentence.strip())

print(sentence.replace("methods", "functions"))
