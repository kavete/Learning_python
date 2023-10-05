print("What's your name?")
name = input()
print("Please tell us your age")
age = int(input())
if (age >= 18) and (age <= 100):
    print("You're welcome " + name)
elif (age < 18) and (age >= 0):
    print("Unauthorised access")
elif (age > 100) and (age < 150):
    print("Really")
else:
    print("Enter a valid value")
