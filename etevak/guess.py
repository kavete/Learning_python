import random
number = random.randrange(1, 10)
print("Welcome to our guessing game")

#  For a range of 1 to 10 and only 5 tries
'''
guess = int(input())
print("Guess a number between 1 and 10\nyou have 5 tries")
for i in range(5):
    if guess > number:
        print("The number is less than " + str(guess))
        print("Guess again")
        guess = int(input())
    elif guess < number:
        print("The number is more than " + str(guess))
        print("Guess again")
        guess = int(input())
    else:
        print("Correct!")
        break
        '''

# unlimited tries
num = random.randrange(1, 100)
print("Enter a number between 1 and 100")
guess = int(input())

count = 0

while True:
    if guess > num:
        print("The number is less than " + str(guess))
        print("Guess again!")
        guess = int(input())
        count += 1
    elif guess < num:
        print("The number is more than " + str(guess))
        print("Guess again!")
        guess = int(input())
        count += 1
    else:
        print("Correct!")
        count += 1
        break
print("You got it in" , count , "tries") 