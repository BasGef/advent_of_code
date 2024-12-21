FILE_NAME = r'aoc2024/day17/input.txt'

def read_code():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    register = {}
    instructions = []

    for line in data:
        if len(line) == 0:
            continue
        datatype, value = line.split(': ')
        if datatype == 'Program':
            instructions = list(map(int, value.split(',')))
            continue
        register[datatype[-1]] = int(value)
    return register, instructions


def adv(operand):
    global register
    register['A'] = register['A'] // 2 ** combo_operand(operand)


def bdv(operand):
    global register
    register['B'] = register['A'] // 2 ** combo_operand(operand)


def bxl(operand):
    global register
    register['B'] = register['B'] ^ operand


def bst(operand):
    global register
    register['B'] = combo_operand(operand) % 8


def cdv(operand):
    global register
    register['C'] = register['A'] // 2 ** combo_operand(operand)


def jnz(operand):
    global register
    global pointer

    if register['A'] == 0:
        return
    pointer = operand - 2  # - 2 negates the jump after execution


def bxc(operand):
    """ operand included for legacy reason. not in use """
    global register
    register['B'] = register['B'] ^ register['C']


def out(operand):
    output = str(combo_operand(operand) % 8)

    # since we need to comma separate all output anyway, no need to do this here
    # if len(output) <= 1:
    return output
    # return ','.join(o for o in output)


def process_instruction(opcode, operand):
    instruction_set = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    return instruction_set[opcode](operand) or ''


def combo_operand(operand):
    global register
    if operand < 0 or operand >= 7:
        raise NotImplementedError(f'Operand should be between 0 and 7. Got {operand}')
    if operand <= 3:
        return operand
    return register[chr(61 + operand)]


if __name__ == '__main__':
    register, instructions = read_code()
    pointer = 0
    output = ''

    while pointer < len(instructions):
        opc, oper = instructions[pointer: pointer + 2]
        output += process_instruction(opc, oper)
        pointer += 2

    answer_17a = ','.join(o for o in output)
    print(f'{answer_17a=}')