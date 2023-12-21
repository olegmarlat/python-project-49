from random import randint

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
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


def get_game():
    question = randint(1, 50)
    correct_answer = is_prime(question)
    return str(question), correct_answer
