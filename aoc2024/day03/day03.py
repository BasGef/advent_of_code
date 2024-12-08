import re
import numpy as np

FILE_PATH = r'./aoc2024/day03/input.txt'


def colvec(array):
    return array.reshape(1, -1)


def rowvec(array):
    return array.reshape(-1, 1)


def simple_mul(data):  # 3a
    regex = r'mul\((\d+),(\d+)\)'
    muls = re.findall(regex, data)
    return sum(int(m[0]) * int(m[1]) for m in muls)


def conditional_mul(data):  # 3b
    # TODO: This must surely be possible with one regex
    matches = re.finditer(regex, data)
    matches = np.array([(m.start(), int(m.group(1)) * int(m.group(2))) for m in matches])

    dos = re.finditer(r'do\(\)', data)
    donts = re.finditer(r'don\'t\(\)', data)
    enabled = sorted([(d.start(), 1) for d in dos] + [(d.start(), 0) for d in donts] + [(0, 1)])
    enabled = np.array(enabled)

    enabled_pos = colvec(enabled[:, 0])
    enabled_values = colvec(enabled[:, 1])
    mult_pos = matches[:, 0].reshape(-1, 1)
    mult_values = matches[:, 1].reshape(-1, 1)
    mult_matrix = np.where(enabled_pos < mult_pos, enabled_values * mult_values, np.nan)

    last_valid = (~np.isnan(aaa)).sum(axis=1) - 1  # only use the last value in each row
    return int(mult_matrix[range(len(mult_matrix)), last_valid].sum())


if __name__ == '__main__':
    with open(FILE_PATH, 'r') as f:
        data = f.read()

    answer_3a = simple_mul(data)
    answer_3b = conditional_mul(data)

    print(f'{answer_3a=}')
    print(f'{answer_3b=}')



