FILE_PATH = './input.txt'

from itertools import pairwise


def q1a():
    with open(FILE_PATH) as file:
        data = [int(x) for x in file.read().splitlines()]
    return sum(b > a for a, b in pairwise(data))


if __name__ == '__main__':
    print(f'{q1a()=}')
