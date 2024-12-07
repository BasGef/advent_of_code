"""
https://adventofcode.com/2022/day/1
"""

FILE_PATH = r'./input.txt'


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def count_calories(n_elves, input_file):
    data = load_data(input_file)

    max_calories = [0] * n_elves
    calories = 0
    for d in data:
        if not d:  # elves are split by blank lines in source file
            min_max = min(max_calories)
            if calories > min_max:
                max_calories[max_calories.index(min_max)] = calories
            calories = 0
            continue
        calories += int(d)
    return sum(max_calories)


if __name__ == '__main__':
    answer_1a = count_calories(1, FILE_PATH)
    answer_1b = count_calories(3, FILE_PATH)
    print(f'{answer_1a=}, {answer_1b=}')