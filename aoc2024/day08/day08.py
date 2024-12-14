import itertools
import numpy as np

FILE_NAME = r'aoc2024/day08/input.txt'

def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = np.array([[c for c in line] for line in data])
    return data


def find_antinodes(antenna_type):
    antinodes = set()
    antennas = [np.array((x, y)) for x, y in zip(*np.where(data==antenna_type))]
    for a0, a1 in itertools.combinations(antennas, 2):
        distance = a1 - a0
        antinodes.add(tuple(a0 - distance))
        antinodes.add(tuple(a1 + distance))
    return antinodes


if __name__ == '__main__':
    data = read_data()

    chars = np.unique(data)
    antinodes = [find_antinodes(char) for char in chars if char != '.']
    antinodes = set(itertools.chain.from_iterable(antinodes))
    antinodes_on_map = list(filter(
        lambda x: (0 <= x[0] < data.shape[0]) and (0 <= x[1] < data.shape[1]),
        antinodes))

    answer_8a = len(antinodes_on_map)
    print(f'{answer_8a=}')