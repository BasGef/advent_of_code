FILE_PATH = './input.txt'

from itertools import pairwise


def load_data(file_path):
    with open(file_path) as file:
        data = [int(x) for x in file.read().splitlines()]
    return data


def q1a():
    data = load_data(FILE_PATH)
    return sum(b > a for a, b in pairwise(data))


def q1b():
    data = load_data(FILE_PATH)
    # Compare overlapping windows->we only have to compare the outermost items
    return sum(b > a for a, b in zip(data, data[3:]))


if __name__ == '__main__':
    print(f'{q1a()=}')
    print(f'{q1b()=}')
