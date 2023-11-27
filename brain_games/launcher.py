import prompt
from random import randint
import random


def game_launch():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('ВОПРОС ИГРЫ?')
    
    # в каждой игре трижды задается вопрос при удачных ответах, иначе проигрыш
    # как это реализовать на практике? при помощи цикла?
      
    #    join = prompt.integer('Your answer: ')
    #   result = math_operator(math, number1, number2)
        if result == join:
            item += 1
            print('Correct!')
        else:
            item = 4
            print(
                f"'{join} is wrong answer ;(."
                f"Correct answer was '{result}'\nLet's "
                f"try again, {name}!")
        if item == 3:
            print(f'Congratulations, {name}!')