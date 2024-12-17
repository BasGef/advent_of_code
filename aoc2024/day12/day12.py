import numpy as np
from collections import defaultdict

FILE_NAME = r'aoc2024/day12/input.txt'
EMPTY_SPACE = ' '  # Make sure this is any single char not used in the garden


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = np.array([[c for c in line] for line in data], dtype='<U4')
    return data


def divide_garden(data):
    areas = defaultdict(np.int64)
    data = np.pad(data.copy(), 1, constant_values=EMPTY_SPACE)
    for row in range(1, data.shape[0] - 1):
        for col in range(1, data.shape[1] - 1):
            if len(data[row, col]) != 1:
                continue
            cur = data[row, col]
            areas[cur] += 1
            data[row, col] = cur + str(areas[cur])
            find_neighbours(row, col, data)
    return data


def find_neighbours(row, col, data):
    for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        cur = data[row, col][0]
        if data[row + r, col + c] != cur:
            continue
        data[row + r, col + c] = data[row, col]
        find_neighbours(row + r, col + c, data)


def fencing_cost(data):
    fencing = sum((data != np.roll(data, shift, axis=(0, 1)))
                  for shift in ((-1, 0), (1, 0), (0, -1), (0, 1)))

    cost = sum(fencing[data == i].sum() * (data == i).sum()
               for i in np.unique(data) if i != EMPTY_SPACE)
    return cost


if __name__ == '__main__':
    garden = read_data()
    garden = divide_garden(garden)
    answer_12a = fencing_cost(garden)

    print(f'{answer_12a=}')