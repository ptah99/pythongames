import random


def guess(x):
    random_number = random.randint(1, x)
    choice = 0
    while choice != random_number:
        choice = int(input(f'Guess a number between 1 and {x}: '))
        if choice < random_number:
            print('sorry, choice too low.')
        elif choice > random_number:
            print('sorry, choice too high')

    print(f'yay, congrats you have guessed the number {random_number} correctly.')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
          guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low=high
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'computer guessed the number , {guess}, correctly!')


guess(100)