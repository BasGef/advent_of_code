from collections import deque

FILE_PATH = r'./input.txt'


class Monkey:
    def __init__(self):
        self.test_value = 0
        self._next_monkeys = [None, None]  # (false_monkey, true_monkey)
        self.items = None
        self.inspection_count = 0

    def throw_items(self, monkeys):
        while len(self.items):
            item = self.inspect(self.items.popleft())
            destination = self.evaluate_worry_level(item)
            monkeys[destination].catch(item)

    def inspect(self, item):
        self.inspection_count += 1
        return self.operation(item) // 3

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


def q11a():
    data = load_data(FILE_PATH)
    monkeys = make_monkeys(data)

    for _ in range(20):
        for monkey in monkeys:
            monkey.throw_items(monkeys)

    monkey_vals = sorted((m.inspection_count for m in monkeys), reverse=True)
    return monkey_vals[0] * monkey_vals[1]


if __name__ == '__main__':
    print(f'{q11a()}')