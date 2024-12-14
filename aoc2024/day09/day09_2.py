import itertools
import numpy as np


FILE_NAME = r'aoc2024/day09/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read()
    data = [[np.NAN if i % 2 else i // 2] * int(d) for i, d in enumerate(data)]
    if len(data) % 2 == 0:
        data = data[:-1]  # remove trailing space
    return data


def defrag_data(data):
    spaces = np.array([len(d) if i % 2 else 0 for i, d in enumerate(data)])
    for i, file in enumerate(data[::-2]):
        space = np.where(spaces >= len(file))[0]
        if len(space) == 0:
            continue
        space = min(space)

        file_index = len(data) - 2 * i - 1
        if space > file_index:
            continue

        offset = len(data[space]) - data[space].count(np.NAN)
        data[space][offset:offset + len(file)] = file
        spaces[space] -= len(file)

        data[file_index] = [np.NAN] * len(file)
        spaces[file_index] = len(file)
    return data


def checksum(data):
    data = list(itertools.chain.from_iterable(data))
    return int(np.nansum(data * np.arange(len(data))))


if __name__ == '__main__':
    data = read_data()
    data = defrag_data(data)
    answer_9b = checksum(data)
    print(f'{answer_9b=}')

