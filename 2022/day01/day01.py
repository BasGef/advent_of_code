"""
https://adventofcode.com/2022/day/1
"""

FILE_PATH = r'./input.txt'


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def question1(input_file):
    data = load_data(input_file)

    max_calories = 0
    calories = 0
    for d in data:
        if not d:  # elves are split by blank lines in source file
            if calories > max_calories:
                max_calories = calories
            calories = 0
            continue
        calories += int(d)
    return max_calories


def question2(n_elves= 3, input_file=FILE_PATH):
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
    print(question1(FILE_PATH))
    print(question2(1, FILE_PATH))
    print(question2(3, FILE_PATH))