from collections import defaultdict

FILE_NAME = r'aoc2024/day05/input.txt'


def process_data(data):
    delimiter = data.index('')
    rules = defaultdict(set)
    for rule in data[:delimiter]:
        page, before_page = map(int, rule.split('|'))
        rules[page].add(before_page)
    updates = [list(map(int, u.split(','))) for u in data[delimiter+1:]]
    return rules, updates


def validate_updates(updates, rules, return_valid=True):
    """ Validates the update according to rules. """
    valid = []
    invalid = []
    for update in updates:
        processed = set()
        for page in update:
            if len(rules[page].intersection(processed)) > 0:
                invalid.append(update)
                break
            processed.add(page)
        else:
            valid.append(update)
    return valid if return_valid else invalid


def fix_update(update, rules):
    update = update.copy()
    swaps = []
    while len(validate_updates([update], rules, False)) > 0:
        processed = set()
        for page in update:
            processed.add(page)
            errors = rules[page].intersection(processed)
            if len(errors) == 0:
                continue
            insert_before = min(update.index(error) for error in errors)
            swaps.append((page, insert_before))

        for page, before in swaps:
            update.remove(page)
            update.insert(before, page)
    return update


def add_middle_pages(updates):
    return sum(update[len(update) // 2] for update in updates)


if __name__ == '__main__':
    with open(FILE_NAME) as f:
        data = f.read().splitlines()

    rules, updates = process_data(data)
    valid_updates = validate_updates(updates, rules)
    answer_5a = add_middle_pages(valid_updates)
    print(f'{answer_5a}')

    invalid_updates = validate_updates(updates, rules, False)
    fixed_updates = [fix_update(update, rules) for update in invalid_updates]
    answer_5b = add_middle_pages(fixed_updates)
    print(f'{answer_5b}')