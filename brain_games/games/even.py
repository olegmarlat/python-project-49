import prompt
from random import randint


def even_game_one():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    item = 0
    while item < 3:
        number = randint(1, 999999999)
        print(f'Question:{number}')
        join = prompt.string('Your answer: ')
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        if answer == join.lower():
            item += 1
            print('Correct!')
        else:
            item = 4
            print(f"'{join}' is wrong answer.")
            print(f'Correct answer was "{answer}"')
            print(f"Let's try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')
