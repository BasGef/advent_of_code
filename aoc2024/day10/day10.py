import numpy as np

FILE_NAME = r'aoc2024/day10/input.txt'


def find_peaks(pos, data):
    if data[tuple(pos)] == 9:
        return {tuple(pos)}

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    peaks = set()
    for d in directions:
        if min(pos + d) < 0 or min(data.shape - (pos + d)) <= 0:  # out of bounds
            continue
        if data[tuple(pos + d)] - data[tuple(pos)] != 1:
            continue
        peaks = peaks.union(find_peaks(pos + d, data))
    return peaks


def rate_trailhead(pos, data):
    if data[tuple(pos)] == 9:
        return 1

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    rating = 0
    for d in directions:
        if min(pos + d) < 0 or min(data.shape - (pos + d)) <= 0:  # out of bounds
            continue
        if data[tuple(pos + d)] - data[tuple(pos)] != 1:
            continue
        rating += rate_trailhead(pos + d, data)
    return rating

if __name__ == '__main__':
    with open(FILE_NAME) as f:
        data = [[int(x) for x in line] for line in f.read().splitlines()]
    data = np.array(data)

    trailheads = [np.array((x, y)) for x, y in zip(*np.where(data == 0))]
    peaks = {tuple(trailhead): find_peaks(trailhead, data) for trailhead in trailheads}
    answer_10a = sum(len(p) for p in peaks.values())

    ratings = {tuple(trailhead): rate_trailhead(trailhead, data) for trailhead in trailheads}
    answer_10b = sum(rating for rating in ratings.values())

