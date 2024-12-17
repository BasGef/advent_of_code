from collections import Counter
import numpy as np

FILE_NAME = r'aoc2024/day14/input.txt'

def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = [[np.array([int(x) for x in c[2:].split(',')]) for c in d.split(' ')] for d in data]
    return data


def quadrant(position, room_size):
    middle = [s // 2 for s in room_size]  # TODO: this expects room size value to be odd
    if any(position == middle):
        return 0
    return sum((position < middle) * (1, 2)) + 1

def safety_value(start_positions, room_size, seconds):
    positions = [np.mod(p + v * seconds, room_size) for p, v in start_positions]
    quadrants = [quadrant(p, room_size) for p in positions]
    count = Counter(quadrants)
    return np.prod([count[q] for q in range(1, 5)])


if __name__ == '__main__':
    data = read_data()
    answer_14a = safety_value(data, (101, 103), 100)
    print(f'{answer_14a=}')
