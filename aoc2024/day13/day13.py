import numpy as np
import re

FILE_NAME = r'aoc2024/day13/input.txt'


def read_data():
    with open(FILE_NAME) as f:
        data = f.read().splitlines()
    buttons_a = [list(map(int, re.findall(r'\d+', d))) for d in data[::4]]
    buttons_b = [list(map(int, re.findall(r'\d+', d))) for d in data[1::4]]
    prizes = [np.array(list(map(int, re.findall(r'\d+', d)))) for d in data[2::4]]
    buttons = [np.array([a, b]).T for a, b in zip(buttons_a, buttons_b)]
    return buttons, prizes


def valuate_claw_machine(buttons, prize, button_cost=(3, 1), max_presses=None):
    presses = np.linalg.solve(buttons, prize)  # TODO: I guess this approach could fail on ambiguous solutions when not including cost of buttons
    if min(presses) < 0 or (max_presses and max(presses) > max_presses):
        return 0
    # if not all(np.isclose(presses, np.round(presses, 0))):
    if not np.allclose(presses, np.round(presses, 0), rtol=0, atol=0.01):
        return 0  # no integer solution
    return sum(presses * button_cost)


if __name__ == '__main__':
    buttons, prizes = read_data()
    cost = sum(valuate_claw_machine(b, p, max_presses=100) for b, p in zip(buttons, prizes))

    answer_13a = int(cost)
    print(f'{answer_13a=}')

    expensive_prizes = [p + 10_000_000_000_000 for p in prizes]
    high_cost = sum(valuate_claw_machine(b, p) for b, p in zip(buttons, expensive_prizes))
    answer_13b = int(high_cost)
    print(f'{answer_13b=}')
