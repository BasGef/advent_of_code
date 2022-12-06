from statistics import mode

FILE_PATH = './input.txt'


def load_data_as_bits(file_path):
    with open(file_path) as f:
        data = [[int(c) for c in l] for l in f.read().splitlines()]
    return data


def most_common_bit_value(data):
    bits = [list(d) for d in zip(*data)]  # pivot number to bit positions
    return [mode(bit) for bit in bits]


def gamma(bits):
    return sum(2 ** pow for pow, is_set in enumerate(reversed(bits)) if is_set)


def epsilon(bits):
    return sum(2 ** pow for pow, is_set in enumerate(reversed(bits)) if not is_set)


def q3a():
    data = load_data_as_bits(FILE_PATH)
    bits = most_common_bit_value(data)
    return gamma(bits) * epsilon(bits)


if __name__ == '__main__':
    print(f'{q3a()=}')