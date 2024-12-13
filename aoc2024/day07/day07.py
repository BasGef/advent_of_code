FILE_NAME = r'aoc2024/day07/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    data = [d.split(':') for d in data]
    data = ((int(s), [int(x) for x in v.strip().split(' ')]) for s, v in data)
    return data


def validate(total, values):
    if len(values) == 1:
        return total == values[0]
    if validate(total, [values[0] * values[1]] + values[2:]):
        return True
    return validate(total, [values[0] + values[1]] + values[2:])


if __name__ == '__main__':
    data = read_data()
    calibration_result = 0
    for total, values in data:
        if validate(total, values):
            calibration_result += total
    answer_7a = calibration_result

