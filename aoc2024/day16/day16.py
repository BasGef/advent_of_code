import numpy as np
from collections import namedtuple, deque, defaultdict

FILE_NAME = r'aoc2024/day16/input.txt'
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
    entry_from = defaultdict(set)  # stores location: cheapest paths to location
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

            cost = visited_nodes[node] + MOVE_COST + (direction != node.dir) * TURN_COST
            if new_node in visited_nodes and cost > visited_nodes[new_node]:
                continue

            if new_node in visited_nodes and cost == visited_nodes[new_node]:
                entry_from[new_node].add(node)
                continue

            visited_nodes[new_node] = cost
            entry_from[new_node] = {node}
            if new_node.row != end.row or new_node.col != end.col:
                open_nodes.append(new_node)
    return visited_nodes, entry_from


def find_optimal_paths(nodes):
    end_states = [Node(end.row, end.col, d) for d in (LEFT, RIGHT, UP, DOWN)]
    end_points = {e: node_cost[e] for e in end_states if e in nodes}
    lowest_cost = min(end_points.values())
    optimal_paths = [path for path, cost in end_points.items() if cost == lowest_cost]
    return lowest_cost, optimal_paths


def find_best_seats(optimal_paths, entry_from):
    nodes = deque(optimal_paths)
    locations = set()
    while len(nodes) != 0:
        node = nodes.pop()
        locations.add(node)
        nodes.extend(entry_from[node])
    # Nodes are stored with direction, so deduplicate to get locations on map
    locations = {(l.row, l.col) for l in locations}
    return locations


if __name__ == '__main__':
    grid = read_data()

    start = Node(*get_coordinates('S', grid)[0], RIGHT)
    end = Node(*get_coordinates('E', grid)[0], None)
    node_cost, entry_from = traverse_maze(grid, start, end)

    lowest_cost, optimal_paths = find_optimal_paths(node_cost)
    answer_16a = lowest_cost
    print(f'{answer_16a=}')

    best_seats = find_best_seats(optimal_paths, entry_from)
    answer_16b = len(best_seats)
    print(f'{answer_16b=}')
