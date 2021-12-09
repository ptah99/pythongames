import random

secret_number = random.randint(1, 10)
chances = 0
guess = print("Guess a number btwn 1 and 10")

while guess != secret_number:
    guess = int(input("Guess: "))
    chances += 1
    if chances > 3:
        print("you failed!")
else:
    print("guessed correctly!")
