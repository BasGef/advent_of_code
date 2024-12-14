import itertools
import numpy as np

# 1317 too low
#

FILE_NAME = r'aoc2024/day08/input.txt'

def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = np.array([[c for c in line] for line in data])
    return data


def find_antinodes(antenna_type, resonance=False, map_size=None):
    antinodes = set()
    antennas = [np.array((x, y)) for x, y in zip(*np.where(data==antenna_type))]
    for a0, a1 in itertools.combinations(antennas, 2):
        distance = a1 - a0
        if not resonance:
            antinodes.add(tuple(a0 - distance))
            antinodes.add(tuple(a1 + distance))
            continue
        origin = (np.array(map_size) - 1) * (distance < 0)
        start = origin + ((a0 - origin) / distance - int(min((a0 - origin) / distance))) * distance
        nodes = {tuple(np.round(start + i * distance, 0)) for i in range(max(map_size))}
        antinodes = antinodes.union(nodes)
    return antinodes


# def antinodes_resonance(antenna_type, map_size):
#     antinodes = set()
#     antennas = [np.array((x, y)) for x, y in zip(*np.where(data==antenna_type))]
#     for a0, a1 in itertools.combinations(antennas,2):
#         distance = a1 - a0
#         origin = (np.array(map_size) - 1) * (distance < 0)
#         start = origin + ((a0 - origin) / distance - int(min((a0 - origin) / distance))) * distance
#         antinodes = antinodes.union({tuple(np.round(start + i * distance, 0)) for i in range(max(map_size))})
#     return antinodes


def flatten_and_filter(antinodes, map_size):
    antinodes = set(itertools.chain.from_iterable(antinodes))
    antinodes = list(filter(
        lambda x: (0 <= x[0] < map_size[0]) and (0 <= x[1] < map_size[1]),
        antinodes))
    return antinodes


if __name__ == '__main__':
    data = read_data()

    chars = np.unique(data)
    antinodes = [find_antinodes(char) for char in chars if char != '.']
    antinodes = flatten_and_filter(antinodes, data.shape)
    answer_8a = len(antinodes)

    antinodes_resonance = [find_antinodes(char, True, data.shape) for char in chars if char != '.']
    antinodes_resonance = flatten_and_filter(antinodes_resonance, data.shape)
    answer_8b = len(antinodes_resonance)

    print(f'{answer_8a=}')
    print(f'{answer_8b=}')
