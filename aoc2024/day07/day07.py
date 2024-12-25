import math
FILE_NAME = r'aoc2024/day07/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = [d.split(':') for d in data]
    data = tuple((int(s), [int(x) for x in v.strip().split(' ')]) for s, v in data)
    return data


def validate(total, values, allow_concat=False):
    if len(values) == 1:
        return total == values[0]
    if validate(total, [values[0] * values[1]] + values[2:], allow_concat):
        return True
    if validate(total, [values[0] + values[1]] + values[2:], allow_concat):
        return True
    if not allow_concat:
        return False
    return validate(total, [concatenate(*values[:2])] + values[2:], True)


def concatenate(value1, value2):
    return value1 * 10 ** (math.floor(math.log10(value2))+1) + value2


if __name__ == '__main__':
    data = read_data()
    calibration_result = 0
    data2 = []
    for total, values in data:
        if validate(total, values):
            calibration_result += total
            continue
        data2.append((total, values))
    answer_7a = calibration_result
    print(f'{answer_7a=}')

    calibration_result2 = 0
    for total, values in data2:
        if validate(total, values, allow_concat=True):
            calibration_result2 += total
    answer_7b = calibration_result + calibration_result2
    print(f'{answer_7b=}')
