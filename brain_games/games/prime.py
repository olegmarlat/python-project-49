import prompt
from random import randint

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def it_prime(num):
    if num < 2:
        return 'no'
    n = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            n += 1
    if n == 0:
        return 'yes'
    else:
        return 'no'


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    item = 0
    while item < 3:
        number1 = randint(1, 50)
        prime = it_prime(number1)
        print(f'Question: {number1}')
        join = prompt.string('Your answer: ')
        if join.lower() == prime:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(
                f"'{join}' is wrong answer ;(. "
                f"Correct answer was '{prime}'\nLet's "
                f"try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')
