from statistics import mode

FILE_PATH = './input.txt'


def load_data_as_bits(file_path):
    with open(file_path) as f:
        data = [[int(c) for c in l] for l in f.read().splitlines()]
    return data


def most_common_bit_value(data):
    bits = [list(d) for d in zip(*data)]  # pivot number to bit positions
    return [0 if bit.count(1) > bit.count(0) else 1 for bit in bits]
    # return [mode(bit) for bit in bits]


def gamma(bits):
    return sum(2 ** pow for pow, is_set in enumerate(reversed(bits)) if is_set)


def epsilon(bits):
    return sum(2 ** pow for pow, is_set in enumerate(reversed(bits)) if not is_set)


def eliminate_numbers(data, type='most_common'):
    i = 0
    while len(data) > 1:
        bits = [d[i] for d in data]
        if type == 'most_common':
            keep_bit = bits.count(1) >= bits.count(0)
        else:
            keep_bit = bits.count(1) < bits.count(0)
        data = [d for d in data if d[i] == keep_bit]
        i += 1
    return sum(2 ** pow for pow, is_set in enumerate(reversed(data[0])) if is_set)


def q3a():
    data = load_data_as_bits(FILE_PATH)
    bits = most_common_bit_value(data)
    return gamma(bits) * epsilon(bits)

def q3b():
    data = load_data_as_bits(FILE_PATH)
    oxygen = eliminate_numbers(data, 'most_common')
    co2 = eliminate_numbers(data, 'least_common')
    return oxygen * co2


if __name__ == '__main__':
    print(f'{q3a()=}')
    print(f'{q3b()=}')
