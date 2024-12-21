import numpy as np
from collections import namedtuple, deque

FILE_NAME = r'aoc2024/day16/sample_input_2.txt'
MOVE_COST = 1
TURN_COST = 1000


Node = namedtuple('Node', ['row', 'col', 'dir'])
Direction = namedtuple('Direction', ['row', 'col'])

RIGHT = Direction(0, 1)
LEFT = Direction(0, -1)
UP = Direction(-1, 0)
DOWN = Direction(1, 0)


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    grid = np.array([[c for c in line] for line in data])
    return grid


def get_coordinates(item, grid):
    return tuple(zip(*np.where(grid == item)))


def traverse_maze(grid, start, end):
    visited_nodes = {start: 0}  # stores location: cost to get there
    open_nodes = deque([start])

    while len(open_nodes) != 0:
        node = open_nodes.pop()
        for direction in (RIGHT, LEFT, UP, DOWN):
            if direction.row + node.dir.row == 0 and direction.col + node.dir.col == 0:  # No turning back
                continue
            new_node = Node(node.row + direction.row, node.col + direction.col,
                            direction)
            if grid[new_node.row, new_node.col] == '#':  # Wall
                continue
            cost = visited_nodes[node] + MOVE_COST + (
                        direction != node.dir) * TURN_COST
            if new_node in visited_nodes and cost >= visited_nodes[new_node]:
                continue

            visited_nodes[new_node] = cost
            if new_node.row != end.row or new_node.col != end.col:
                open_nodes.append(new_node)
    return visited_nodes


if __name__ == '__main__':
    grid = read_data()

    start = Node(*get_coordinates('S', grid)[0], RIGHT)
    end = Node(*get_coordinates('E', grid)[0], None)
    node_cost = traverse_maze(grid, start, end)
    end_states = [Node(end.row, end.col, d) for d in (LEFT, RIGHT, UP, DOWN)]
    answer_16a = min(node_cost[e] for e in end_states if e in node_cost)
