import prompt


def game_launch(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_TASK)
    rounds_count = 3
    for n in range(rounds_count):
        question, correct_answer = game.game_flow()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer:')

        if player_answer != correct_answer:
            print(f"'{player_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        else:
            print('Correct!')

    else:
        print(f'Congratulations, {name}!')
