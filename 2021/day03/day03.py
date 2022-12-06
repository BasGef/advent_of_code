from statistics import mode

FILE_PATH = './input.txt'


def q3a():
    with open(FILE_PATH) as f:
        data = [[int(c) for c in l] for l in f.read().splitlines()]
    bits = [list(d) for d in zip(*data)]  # pivot number to bit positions
    most_sig = [mode(bit) for bit in bits]
    gamma = sum(2 ** pow for pow, is_set in enumerate(reversed(most_sig)) if is_set)
    epsilon = sum(2 ** pow for pow, is_set in enumerate(reversed(most_sig)) if not is_set)
    return gamma * epsilon


if __name__ == '__main__':
    print(f'{q3a=}')