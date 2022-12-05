"""
https://adventofcode.com/2022/day/5
"""

import re

FILE_PATH = r'./input.txt'

def load_data(file_path: str):
    with open(file_path) as file:
        data = file.read().splitlines()
    delim = data.index('')  # empty line delineates the two data sets
    return data[:delim], data[delim+1:]


def clean_stacks_data(stacks):
    stacks = reversed(stacks[:-1])
    stacks = [row[1::4] for row in stacks]
    stacks = [list(col) for col in zip(*stacks)]  # 'pivots' the lists.
    return [s if ' ' not in s else s[:s.index(' ')] for s in stacks]  # remove empties


def clean_moves_data(moves):
    return [tuple(int(d) for d in re.findall(r'\d+', move)) for move in moves]


stacks, moves = load_data(FILE_PATH)
stacks = clean_stacks_data(stacks)
moves = clean_moves_data(moves)


