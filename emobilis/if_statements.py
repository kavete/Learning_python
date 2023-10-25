height_in_metres = 1.8
weight_in_kgs = 70

bmi = weight_in_kgs / height_in_metres ** 2

print(f"BMI is { bmi }")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("Normal weight")
elif bmi >= 24.9 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")

if 10 == 10.00:
    print("Equal")
else:
    print("Not equal")

sentence = "Kenya, Uganda and Tanzania"

if "kenya" in sentence.lower():
    print("It exists")
else:
    print("It doesn't exist")

