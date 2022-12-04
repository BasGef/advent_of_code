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


def win_lose(other_hand, own_hand):
    # There are only 3 choices, and in each case choice loses to choice + 1
    # (e.g. Rock < Paper; Paper < Scissors; Scissors < Rock).
    # So we can use mod 3 to determine results:
    if own_hand == other_hand:
        return Result.TIE
    if (own_hand + 1) % 3 == other_hand:
        return Result.LOSS
    return Result.WIN


if __name__ == '__main__':
    with open(FILE_PATH, 'r') as file:
        matches = file.read().splitlines()

    score = len(matches)  # Hands base 0; scoring begins at 1 -> add 1 per match
    for match in matches:
        hands = [Hand[h] for h in match.split()]
        score += win_lose(*hands) * 3
        score += hands[1]
