from __future__ import annotations
from itertools import pairwise

FILE_PATH = r'input.txt'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_adjacent(self, other: Point):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    @property
    def coords(self):
        return self.x, self.y

    def move(self, direction: str, steps: int):
        if direction == 'U':
            self.y += steps
        elif direction == 'D':
            self.y -= steps
        elif direction == 'R':
            self.x += steps
        else:
            self.x -= steps

    def follow(self, other: Point):
        if self.is_adjacent(other):
            return None

        x_dir = (other.x - self.x) // (abs(other.x - self.x)) if self.x != other.x else 0
        y_dir = (other.y - self.y) // (abs(other.y - self.y)) if self.y != other.y else 0
        # first step may be diagonal. assume either d(x) or d(y) always (1, -1)
        if x_dir and y_dir:
            self.x, self.y = self.x + x_dir, self.y + y_dir
            steps = [self.coords]
        else:
            steps = []

        if self.x == other.x:
            steps += [(self.x, y) for y in range(self.y + y_dir, other.y, y_dir)]
        else:
            steps += [(x, self.y) for x in range(self.x + x_dir, other.x, x_dir)]
        self.x, self.y = steps[-1]
        return steps

    def __repr__(self):
        return f"Point ({self.x}, {self.y})"


def q9a():
    with open(FILE_PATH) as file:
        moves = file.read().splitlines()

    head = Point(0, 0)
    tail = Point(0, 0)
    visited = {tail.coords}

    # TODO: make animation of sequence of moves of head, tail in a grid
    for move in moves:
        direction, steps = move.split(' ')
        head.move(direction, int(steps))
        steps = tail.follow(head)
        if steps:
            visited.update(steps)
    return len(visited)


def q9b():
    # simply q9a but recursively for points H through 9

    with open(FILE_PATH) as file:
        moves = file.read().splitlines()

    points = {i: Point(0,0) for i in range(10)}
    head = points[0]
    tail = points[9]
    visited = {tail.coords}

    for move in moves:
        direction, steps = move.split(' ')
        for step in range(1, int(steps) + 1):
            head.move(direction, 1)
            for leader, follower in pairwise(points.values()):
                steps = follower.follow(leader)
                if follower is tail and steps:
                    visited.update(steps)
    return len(visited)


if __name__ == '__main__':
    print(f'{q9a()=}')
    print(f'{q9b()=}')