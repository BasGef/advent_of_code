"""
https://adventofcode.com/2022/day/1
"""

FILE_PATH = r'./input.txt'


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


if __name__ == '__main__':
    data = load_data(FILE_PATH)

    max_calories = 0
    calories = 0
    for d in data:
        if not d:  # elves are split by blank lines in source file
            if calories > max_calories:
                max_calories = calories
            calories = 0
            continue
        calories += int(d)
    # return max_calories
    print(max_calories)