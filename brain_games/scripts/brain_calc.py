#!/usr/bin/env python3


from brain_games.launcher import game_launch
from brain_games.games.calc import game_calc


def main():
    game_launch(game_calc)


if __name__ == '__main__':
    main()
