import numpy as np

FILE_NAME = r'aoc2024/day20/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    grid = np.array([[c for c in line] for line in data])
    return grid


def get_coordinates(item, grid):
    return tuple(zip(*np.where(grid == item)))


def compute_distance_to_exit(grid):
    start = get_coordinates('S', grid)[0]
    end = get_coordinates('E', grid)[0]

    distance = np.zeros_like(grid, dtype=float)
    distance[:] = np.nan

    pos = end
    distance[end] = 0
    while pos != start:
        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_pos = pos[0] + direction[0], pos[1] + direction[1]
            if grid[new_pos] == '#':
                continue
            if not np.isnan(distance[new_pos]):
                continue
            distance[new_pos] = distance[pos] + 1
            pos = new_pos
            break  # no need to check other directions
    return distance

def find_shortcuts(grid, distance):
    shortcuts_lr = np.where(
        grid == '#', np.abs(np.roll(distance, 1) - np.roll(distance, -1)) - 2, np.nan)
    shortcuts_ud = np.where(
        grid == '#', np.abs(np.roll(distance, 1, 0) - np.roll(distance, -1, 0)) - 2, np.nan)
    shortcuts = np.hstack([shortcuts_lr[~np.isnan(shortcuts_lr)],
                           shortcuts_ud[~np.isnan(shortcuts_ud)]])
    return shortcuts


if __name__ == '__main__':
    grid = read_data()
    distance = compute_distance_to_exit(grid)
    shortcuts = find_shortcuts(grid, distance)
    answer_20a = (shortcuts >= 100).sum()
