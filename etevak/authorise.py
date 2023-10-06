# Ask for user's name
print("What's your name?")
name = input()

# Ask for user's age
print("Please tell us your age")
age = int(input())

# Authorise if age is in the required range
if (age >= 18) and (age <= 100):
    print("You're welcome " + name)
elif (age < 18) and (age >= 0):
    print("Unauthorised access")
elif (age > 100) and (age < 150):
    print("Really")
else:
    print("Enter a valid value")
