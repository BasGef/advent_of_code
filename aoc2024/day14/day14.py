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


def draw_map(data, room_size, second):
    room = np.zeros(room_size)
    positions = [tuple(np.mod(p + v * second, (101, 103))) for p, v in data]
    rows, cols = zip(*positions)
    room[rows, cols] = 1
    return room


def find_tree(data, room_size, maxiter=1_000_000):
    """ Try to find a Christmas tree we don't know the shape of """
    for second in range(maxiter):
        cur_map = draw_map(data, room_size, second)

        # pray this tree is drawing is solid and not an outline
        line_sum = cur_map.sum(axis=0)
        if max(line_sum) < len(data) * 0.05:  # >5% must be in a line for tree?
            continue
        biggest_line = cur_map[:, np.where(line_sum == max(line_sum))[0][0]]
        ones = np.where(biggest_line == 1)[0]
        if ones[-5] - ones[5] > len(data) * 0.05:  # make sure bots are adjacent
            continue
        return second


if __name__ == '__main__':
    data = read_data()
    answer_14a = safety_value(data, (101, 103), 100)
    print(f'{answer_14a=}')

    answer_14b = find_tree(data, (101, 103))
    print(f'{answer_14b=}')