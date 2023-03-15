import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ')
        if int(guess) < random_number:
            print('Sorry, guess again. Too low.')
        elif int(guess) > random_number:
            print('Sorry, guess again. Too high')
        else:
            print(f'Yay, congats. You have guessed the number {random_number} correctly!!!')
            exit()


guess(10)