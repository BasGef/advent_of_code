from typing import Set, List

FILE_PATH = './input.txt'


def numbers_to_set(numbers: str) -> Set[int]:
    return {int(n) for n in numbers.split(' ') if n}


def card_matches(card: str) -> int:
    numbers, winning = card.split(':')[1].split('|')
    numbers = numbers_to_set(numbers)
    winning = numbers_to_set(winning)
    return len(numbers.intersection(winning))


def value_card(card: str):
    return int(2 ** (card_matches(card) - 1))


def count_cards(cards: List[str]) -> dict:
    counter = {i: 1 for i in range(1, len(cards) + 1)}  # initial cards
    for num, card in enumerate(cards, 1):
        for i in range(num + 1, num + value_card_4b(card) + 1):
            if i > len(cards):
                break
            counter[i] += counter[num]
    return counter


if __name__ == '__main__':
    with open(FILE_PATH) as f:
        cards = f.read().splitlines()

    answer_4a = sum(value_card(card) for card in cards)
    answer_4b = sum(count_cards(cards).values())
    print(f'{answer_4a=}')
    print(f'{answer_4b=}')