from collections import namedtuple, deque

FILE_NAME = r'aoc2024/day24/input.txt'

Gate = namedtuple('Gate', ['inputs', 'output', 'operation'])


def compute(gate):
    global values

    if gate.inputs[0] not in values:
        compute(gates[gate.inputs[0]])
    if gate.inputs[1] not in values:
        compute(gates[gate.inputs[1]])

    if gate.operation == 'AND':
        values[gate.output] = values[gate.inputs[0]] & values[gate.inputs[1]]
    elif gate.operation == 'OR':
        values[gate.output] = values[gate.inputs[0]] | values[gate.inputs[1]]
    else: #xor
        values[gate.output] = values[gate.inputs[0]] ^ values[gate.inputs[1]]


def read_data():
    values = {}
    gates = {}
    with open(FILE_NAME) as f:
        for line in f.read().splitlines():
            if line == '':
                continue
            if line[3] == ':':
                variable, value = line.split(': ')
                values[variable] = int(value)
                continue
            in1, oper, in2, _, out = line.split()
            gates[out] = Gate(inputs=(in1, in2), output=out, operation=oper)
    return values, gates


if __name__ == '__main__':
    values, gates = read_data()
    compute_list = sorted(gates.keys())  # avoid computing redundant gates if there are any
    while compute_list and compute_list[-1].startswith('z'):
        compute(gates[compute_list.pop()])

    binary = ''.join(str(values[var]) for var in sorted(filter(lambda x:x.startswith('z'), values), reverse=True))
    answer_24a = int(binary, 2)
    print(f'{answer_24a=}')