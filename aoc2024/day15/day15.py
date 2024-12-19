import numpy as np

FILE_NAME = r'aoc2024/day15/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    delimiter = data.index('')
    grid = np.array([[c for c in line] for line in data[:delimiter]])
    moves = [c for line in data[delimiter:] for c in line]
    return grid, moves


def execute_moves(grid, moves):
    grid = grid.copy()
    for i, move in enumerate(moves):
        rotation = '>^<v'.index(move)
        grid = np.rot90(grid, -rotation)
        # now, can always execute "move right"
        move_right(grid)
        grid = np.rot90(grid, rotation)
    return grid


def move_right(grid):
    """ Moves right in grid. Modifies input data; does not return new grid"""
    row, col = (np.where(grid == '@')[i][0] for i in range(2))
    empties = np.where(grid[row, col:] == '.')[0]
    walls = np.where(grid[row, col:] == '#')[0]
    if empties.size == 0 or walls[0] < empties[0]:  # no possible move
        return
    grid[row, col:col + empties[0] + 1] = np.roll(grid[row, col:col + empties[0] + 1], 1)
    return


def box_coordinates(grid):
    boxes = np.where(grid == 'O')
    return [row * 100 + col for row, col in zip(*boxes)]


if __name__ == '__main__':
    grid, moves = read_data()
    result = execute_moves(grid, moves)
    answer_15a = sum(box_coordinates(result))