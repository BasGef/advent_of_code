"""
https://adventofcode.com/2022/day/2
"""

from enum import IntEnum

FILE_PATH = r'./input.txt'


class Result(IntEnum):
    LOSS = 0
    TIE = 1
    WIN = 2


class Hand(IntEnum):
    # A == X == 'rock'
    # B == Y == 'paper'
    # C == Z == 'scissors'
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    A = ROCK
    B = PAPER
    C = SCISSORS
    X = ROCK
    Y = PAPER
    Z = SCISSORS


def win_lose(other_hand: Hand, own_hand: Hand) -> Result:
    # There are only 3 choices, and in each case choice loses to choice + 1
    # (e.g. Rock < Paper; Paper < Scissors; Scissors < Rock).
    # So we can use mod 3 to determine results:
    if own_hand == other_hand:
        return Result.TIE
    if (own_hand + 1) % 3 == other_hand:
        return Result.LOSS
    return Result.WIN

def load_data(file_path: str):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def q2a():
    matches = load_data(FILE_PATH)
    matches = [tuple(Hand[h] for h in match.split()) for match in matches]
    return sum(win_lose(*match) for match in matches) * 3 + \
           sum(match[1] for match in matches) + len(matches)  # Hands are base 0 -> add 1 per match


def elf_strategy(opponent_hand, strategy):
    """
    Returns the score of a match when using the elf's strategy as given in
    question 2b.
    """
    if strategy == 'Y':  # Tie
        return Hand[opponent_hand] + 1 + Result.TIE * 3
    if strategy == 'X':  # Lose
        return (Hand[opponent_hand] - 1) % 3 + 1
    return (Hand[opponent_hand] + 1) % 3 + 1 + Result.WIN * 3


def q2b():
    matches = load_data(FILE_PATH)
    return sum(elf_strategy(*match.split()) for match in matches)


if __name__ == '__main__':
    print(f'{q2a()=}')
    print(f'{q2b()=}')





