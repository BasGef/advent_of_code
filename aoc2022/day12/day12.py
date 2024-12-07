import numpy as np
import heapq

FILE_PATH = r'./input.txt'
MAX_ELEVATION_DIFF = 1

# class Node:
#     def __init__(self, x, y, elevation):
#         self.x = x
#         self.y = y
#         self.elevation = elevation
#         self.edges = {}


class Graph:
    def __init__(self):
        self.edges = {}

    def neighbours(self, node):
        return self.edges[node]

    def from_grid(self, grid):
        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                self.edges[(row, col)] = get_edges(grid, (row, col))
        return self

    def find_route(self, start, destination):
        """ A* pathfinding implementation """
        queue = PriorityQueue()
        queue.add(start, 0)
        steps = {start: None}
        cost = {start: 0}

        while not queue.is_empty():
            node = queue.get()
            if node == destination:
                break

            for neighbour in self.neighbours(node):
                new_cost = cost[node] + 1  # TODO: cost implementation into graph?
                if neighbour not in cost or new_cost < cost[neighbour]:
                    cost[neighbour] = new_cost
                    priority = new_cost + self.heuristic(neighbour, destination)
                    queue.add(neighbour, priority)
                    steps[neighbour] = node

        if node != destination:
            return None  # failed to find a path
        # retrace steps to give best path
        path = retrace_path(steps, destination, start)
        return path

    @staticmethod
    def heuristic(position, destination):
        return abs(position[0] - destination[0]) + abs(position[1] - destination[1])


class PriorityQueue:
    def __init__(self):
        # heapq uses empty list: https://docs.python.org/3/library/heapq.html
        self.queue = []

    def is_empty(self) -> bool:
        return not self.queue

    def add(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def get(self):
        return heapq.heappop(self.queue)[1]




def retrace_path(route, end, start):
    path = []
    node = end
    while node != start:
        path.append(node)
        node = route[node]
    return path[::-1]

def read_grid(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return np.array([[c for c in line] for line in data])


def get_edges(grid, node):
    edges = []
    for offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        neighbour = node[0] + offset[0], node[1] + offset[1]
        if neighbour[0] < 0 or neighbour[1] < 0:
            continue
        if neighbour[0] >= grid.shape[0] or neighbour[1] >= grid.shape[1]:
            continue
        if grid[neighbour] - grid[node] > MAX_ELEVATION_DIFF:
            continue
        edges.append(neighbour)
    return edges

def elevation_grid(grid):
    grid[grid=='S'] = 'a'
    grid[grid=='E'] = 'z'
    grid = grid.view(np.int32) - 96
    return grid


def get_location(grid, point):
    locs = np.where(grid==point)
    return [loc for loc in zip(locs[0], locs[1])]


def make_graph(grid):
    graph = Graph()
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            graph.edges[(row, col)] = get_edges(grid, (row, col))


def q12a(grid, start, destination):
    graph = Graph().from_grid(grid)
    path = graph.find_route(start, destination)
    return len(path)

def q12b(grid, destination):
    start = get_location(grid, 1)
    graph = Graph().from_grid(grid)
    shortest_path = grid.shape[0] * grid.shape[1]  # arbitrarily large start val
    for s in start:
        path = graph.find_route(s, destination)
        if path is not None and len(path) < shortest_path:
            shortest_path = len(path)
    return shortest_path


def main():
    grid = read_grid(FILE_PATH)
    start = get_location(grid, 'S')[0]
    end = get_location(grid, 'E')[0]
    # Convert to numeric elevation
    grid = elevation_grid(grid)
    print(f'{ q12a(grid,start,end)=}')
    print(f'{ q12b(grid,end)=}')


if __name__ == '__main__':
    main()

