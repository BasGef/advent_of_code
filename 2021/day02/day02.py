FILE_PATH = './input.txt'


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def get_position(moves):
    horizontal, depth = 0, 0
    for move in moves:
        direction, step = move.split(' ')
        if direction == 'forward':
            horizontal += int(step)
            continue
        depth += int(step) * (1 if direction == 'down' else -1)
    return horizontal, depth


def q2a():
    moves = load_data(FILE_PATH)
    horiz, depth = get_position(moves)
    return horiz * depth


if __name__ == '__main__':
    print(f'{q2a()=}')