import json

FILE_PATH = r'./test_input.txt'


def load_data(file_path):
    with open(file_path) as file:
        data = [json.loads(line) for line in file.readlines() if line.strip()]


    # file contains pairs of packets; separated by space; join them together
    return list(zip(data[::2], data[1::2]))


def is_ordered(first, second):
    if isinstance(first, int) and isinstance(second, int):
        return first <= second
    if isinstance(first, int):
        return is_ordered([first], second)
    if isinstance(second, int):
        return is_ordered(first, [second])
    # if len(second) < len(first):
    #     return False
    for f, s in zip(first, second):
        if not is_ordered(f, s):
            return False
    return True

data = load_data(FILE_PATH)
count = 0
for i, pair in enumerate(data, 1):
    if is_ordered(*pair):
        print(i)
        count += i