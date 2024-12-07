import turtledemo.penrose
from collections import deque
import math

FILE_PATH = r'./input.txt'


class Monkey:
    def __init__(self):
        self.test_value = 0
        self._next_monkeys = [None, None]  # (false_monkey, true_monkey)
        self.items = None
        self.inspection_count = 0
        self.item_modulus = 1

    def throw_items(self, monkeys, lower_worry_level=True):
        while len(self.items):
            item = self.inspect(self.items.popleft(), lower_worry_level)
            destination = self.evaluate_worry_level(item)
            monkeys[destination].catch(item)

    def inspect(self, item, lower_worry_level=True):
        self.inspection_count += 1
        if lower_worry_level:
            return (self.operation(item) // 3) % self.item_modulus
        return self.operation(item) % self.item_modulus

    def evaluate_worry_level(self, item):
        return self._next_monkeys[item % self.test_value == 0]

    @staticmethod
    def operation(item):
        pass

    def catch(self, item):
        self.items.append(item)

    def set_true_monkey(self, value):
        self._next_monkeys[True] = value

    def set_false_monkey(self, value):
        self._next_monkeys[False] = value


def make_function(rule):
    *_, oper, other = rule.split()
    if other == 'old':
        return lambda x: x ** 2
    if oper == '+':
        return lambda x: x + int(other)
    return lambda x: x * int(other)


def load_data(file_path):
    with open(file_path) as file:
        data = file.read().splitlines()
    return data


def make_monkeys(data):
    monkeys = []
    for line in data:
        if not line:
            monkeys.append(monkey)
            continue
        if line.startswith('Monkey'):
            monkey = Monkey()
        key, val = line.split(':')
        if key == '  Starting items':
            monkey.items = deque(int(i) for i in val.split(','))
        if key == '  Operation':
            monkey.operation = make_function(val)
        if key == '  Test':
            monkey.test_value = int(val.split(' ')[-1])
        if key == '    If true':
            monkey.set_true_monkey(int(val.split(' ')[-1]))
        if key == '    If false':
            monkey.set_false_monkey(int(val.split(' ')[-1]))
    monkeys.append(monkey)
    return monkeys


def safe_modulus(monkeys):
    """
    Returns the safe modulus for any item <> monkey combination. Note that each
    monkey has its own PRIME as the test_value. We can therefore safely reduce
    the size of item by taking the item % mod where mod==prod(test_values)
    """
    return math.prod((m.test_value for m in monkeys))


def monkey_business_level(iterations=20, reset_worry_level=True):
    data = load_data(FILE_PATH)
    monkeys = make_monkeys(data)

    modulus = safe_modulus(monkeys)  # This is needed for part 2 performance
    for monkey in monkeys:
        monkey.item_modulus = modulus

    for _ in range(iterations):
        for monkey in monkeys:
            monkey.throw_items(monkeys, reset_worry_level)

    monkey_vals = sorted((m.inspection_count for m in monkeys), reverse=True)
    return monkey_vals[0] * monkey_vals[1]


if __name__ == '__main__':
    print(f'q11a={monkey_business_level(20, True)}')
    print(f'q11b={monkey_business_level(10_000, False)}')