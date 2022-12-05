"""
https://adventofcode.com/2022/day/5
"""

import re
from typing import Tuple, List

FILE_PATH = r'./input.txt'


def load_data(file_path: str) -> Tuple[List[str], List[str]]:
    with open(file_path) as file:
        data = file.read().splitlines()
    delim = data.index('')  # empty line delineates the two data sets
    return data[:delim], data[delim+1:]


def clean_stacks_data(stacks: List[str]) -> List[List[str]]:
    stacks = reversed(stacks[:-1])
    stacks = [row[1::4] for row in stacks]
    stacks = [list(col) for col in zip(*stacks)]  # 'pivots' the lists.
    return [s if ' ' not in s else s[:s.index(' ')] for s in stacks]  # remove empties


def clean_moves_data(moves: List[str]) -> List[Tuple[int, int, int]]:
    return [tuple(int(d) for d in re.findall(r'\d+', move)) for move in moves]


def q5a():
    stacks, moves = load_data(FILE_PATH)
    stacks = clean_stacks_data(stacks)
    moves = clean_moves_data(moves)

    # TODO: There must be a more efficient way than this?
    for (num, fro, to) in moves:
        stacks[to-1] += stacks[fro-1][:-num-1:-1]
        stacks[fro-1] = stacks[fro-1][:-num]

    return ''.join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    print(f'{q5a()=}')