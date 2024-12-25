import itertools
import math
FILE_NAME = r'aoc2024/day07/input.txt'

# 31131748701538 is too low
# 52820837998879 is too low


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = [d.split(':') for d in data]
    data = tuple((int(s), [int(x) for x in v.strip().split(' ')]) for s, v in data)
    return data


def validate(total, values):
    if len(values) == 1:
        return total == values[0]
    if validate(total, [values[0] * values[1]] + values[2:]):
        return True
    return validate(total, [values[0] + values[1]] + values[2:])


def concatenate(value1, value2):
    return value1 * 10 ** (math.floor(math.log10(value2))+1) + value2


def validate2(total, values):
    if len(values) == 1:
        return total == values[0]
    if sum(values[:2]) > total:
        return False
    if validate2(total, [values[0] * values[1]] + values[2:]):
        return True
    if validate2(total, [values[0] + values[1]] + values[2:]):
        return True
    # return validate2(total, [concatenate(values[0], values[1])] + values[2:])
    for i in range(len(values) - 1):
        if validate2(total, values[:i] + [concatenate(*values[i:i+2])] + values[i+2:]):
            return True
    return False

def validate3(total, values):
    if len(values) == 1:
        return total == values[0]
    if sum(values[:2]) > total:
        return False
    if validate3(total, [values[0] * values[1]] + values[2:]):
        return True
    if validate3(total, [values[0] + values[1]] + values[2:]):
        return True
    # return validate2(total, [concatenate(values[0], values[1])] + values[2:])
    for i in range(len(values) - 1):
        if validate3(total, [concatenate3(values[:i+2])] + values[i+2:]):
            return True
    return False


def concatenate3(values):
    return int(''.join(map(str, values)))


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

    calibration_result2 = 0
    cur = 0
    for total, values in data2:
        print(cur, total, values)
        # if validate2(total, values):
        if validate3(total, values):
            calibration_result2 += total
        cur += 1
    answer_7b = calibration_result + calibration_result2
