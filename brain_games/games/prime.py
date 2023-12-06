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


def game_flow():
    item = 0
    while item < 3:
        question = randint(1, 50)
        correct_answer = it_prime(question)
    return question, correct_answer
