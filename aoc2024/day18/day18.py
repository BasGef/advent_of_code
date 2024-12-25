import numpy as np

FILE_NAME = r'aoc2024/day18/input.txt'
GRID_SIZE = (71, 71)
BYTES = 1024


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = [tuple(map(int, d.split(','))) for d in data]
    return data


def make_grid(size, walls):
    grid = np.zeros(size, '<U1')
    x, y = zip(*walls)
    grid[(y, x)] = '#'
    return grid


def find_paths(grid, start_coordinate, exit_coordinate):
    open_coordinates = [start_coordinate]
    visited = {start_coordinate: 0}

    while open_coordinates:
        coordinate = open_coordinates.pop()
        for step in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            new_coordinate = coordinate[0] + step[0], coordinate[1] + step[1]
            if not 0 <= new_coordinate[0] < grid.shape[0] or \
                    not 0 <= new_coordinate[1] < grid.shape[1]:
                continue  # out of bounds
            if grid[new_coordinate] == '#':
                continue  # wall
            if new_coordinate in visited and visited[new_coordinate] <= visited[coordinate] + 1:
                continue  # cheaper option found

            visited[new_coordinate] = visited[coordinate] + 1
            if new_coordinate == exit_coordinate:
                break  # no need to test other directions
            open_coordinates.append(new_coordinate)
    return visited


if __name__ == '__main__':
    data = read_data()
    grid = make_grid(GRID_SIZE, data[:BYTES])

    start_coordinate = (0, 0)
    exit_coordinate = tuple(np.array(grid.shape) - 1)
    paths = find_paths(grid, start_coordinate, exit_coordinate)
    answer_18a = paths[exit_coordinate]

    print(f'{answer_18a}')


