import numpy as np
from enum import IntEnum

FILE_NAME = r'aoc2024/day06/input.txt'


class Direction(IntEnum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def turn(self):
        return Direction(self.value % 4 + 1)


class Position:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


def read_map_data():
    with open(FILE_NAME) as f:
        data = f.read()
    data = np.array([[char for char in line] for line in data.splitlines()])
    return data


if __name__ == '__main__':
    data = read_map_data()

    if '^' in data:
        direction = Direction.UP
    if '>' in data:
        direction = Direction.RIGHT
    if 'v' in data:
        direction = Direction.DOWN
    if '<' in data:
        direction = Direction.LEFT

    pos = np.where(data == '^')
    pos = (pos[0][0], pos[1][0])

    # TODO: this requires a major refactor
    while True:
        if direction == Direction.UP:
            obstacles = np.where(data[:pos[0], pos[1]] == '#') # only care about rows
            if len(obstacles[0]) == 0:
                data[:pos[0], pos[1]] = 'X'
                break
            next_pos = (max(obstacles[0]) + 1, pos[1])
            data[next_pos[0]:pos[0]+1, pos[1]] = 'X'
        if direction == Direction.DOWN:
            obstacles = np.where(data[pos[0]:, pos[1]] == '#')  # only care about rows
            if len(obstacles[0]) == 0:
                data[pos[0]:, pos[1]] = 'X'
                break
            next_pos = (pos[0] + min(obstacles[0]) - 1, pos[1])
            data[pos[0]:next_pos[0]+1, pos[1]] = 'X'
        if direction == Direction.RIGHT:
            obstacles = np.where(data[pos[0], pos[1]:] == '#')  # only care about columns
            if len(obstacles[0]) == 0:
                data[pos[0], pos[1]:] = 'X'
                break
            next_pos = (pos[0], pos[1] + min(obstacles[0])-1)
            data[pos[0], pos[1]:next_pos[1]+1] = 'X'
        if direction == Direction.LEFT:
            obstacles = np.where(data[pos[0], :pos[1]] == '#')  # only care about columns
            if len(obstacles[0]) == 0:
                data[pos[0], :pos[1]] = 'X'
                break
            next_pos = (pos[0], max(obstacles[0])+1)
            data[pos[0], next_pos[1]:pos[1]+1] = 'X'
        pos = next_pos
        direction = direction.turn()

    answer_6a = len(data[data=='X'])
