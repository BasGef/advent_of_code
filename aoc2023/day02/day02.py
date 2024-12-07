from typing import Set, List
import math
import re

FILE_PATH = r'./input.txt'


class CubeCount:
    def __init__(self, color, count):
        self.color = color
        self.count = count


def cube_count(game: str) -> Set[CubeCount]:
    cubes = re.findall(r'((\d+) (\w+))', game)
    return (CubeCount(key, int(value)) for _, value, key in cubes)


def is_game_possible(game: str, max_cubes: dict) -> bool:
    cubes = cube_count(game)
    for cube in cubes:
        if cube.count > max_cubes[cube.color]:
            return False
    return True


def game_id(game: str):
    return int(re.match(r'Game (\d+):', game)[1])


def possible_games(data: List[str], max_cubes: dict):
    return [game_id(game) for game in data if is_game_possible(game, max_cubes)]


def cube_power(game: str) -> int:
    min_cubes = {'red': 0, 'blue': 0, 'green': 0}
    for cubes in cube_count(game):
        min_cubes[cubes.color] = max(min_cubes[cubes.color], cubes.count)
    return math.prod(min_cubes.values())


if __name__ == '__main__':
    with open(FILE_PATH) as f:
        games = f.read().splitlines()

    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    answer_2a = sum(game_id(game) for game in games
                    if is_game_possible(game, max_cubes))
    answer_2b = sum(cube_power(game) for game in games)

    print(f'{answer_2a=}')
    print(f'{answer_2b=}')
