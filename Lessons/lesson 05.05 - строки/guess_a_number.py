import random

target = random.randint(1, 10)

guess = input("Guess a number from 1 to 10: ")
if target == int(guess):
    print("Correct!")
else:
    print("Looooooooser!")