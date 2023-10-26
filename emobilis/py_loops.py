
from time import sleep
starting_point = input("Enter the starting point > ")
stopping_point = input("Enter the stopping point > ")


# print(type(starting_point))

if starting_point.isnumeric() and stopping_point.isnumeric():

    starting_point = int(starting_point)
    stopping_point = int(stopping_point)

    while starting_point <= stopping_point:
        print(f"Counting { starting_point }")
        sleep(4)
        starting_point+=5
else:
    print("Invalid values")