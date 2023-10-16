import prompt
from random import randint
import math


def game_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")
    item = 0
    while item < 3:
        number1 = randint(1, 10)
        number2 = randint(100, 150)





            print(
                f"'{join}' is wrong answer ;(. "
                f"Correct answer was '{result}'\nLet's "
                f"try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')
