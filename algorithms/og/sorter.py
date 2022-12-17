import random
from typing import Optional


def standard_deck() -> list[tuple[str, int]]:
    return [(s, r) for s in ('C', 'D', 'H', 'S') for r in range(1, 14)]

# To consider
# - a class to represent a card (or a named tuple)
# - threading (specify sorter is not thread safe or add locks)
# - unit tests
# - add iterator or generator to show off
#


class MultiDeckSorter:

    def __init__(self, num_decks: int = 2) -> None:
        if num_decks < 1:
            raise ValueError(f'Minimum number of decks is 1 ({num_decks} specified)')
        self._cards = standard_deck() * num_decks
        self._next_index = 0
        self._total_cards = len(self._cards)

    def reset(self) -> None:
        random.shuffle(self._cards)
        self._next_index = 0

    def next_card(self) -> Optional[tuple[str, int]]:
        card = None
        if self._next_index < self._total_cards:
            card = self._cards[self._next_index]
            self._next_index += 1
        return card

    def remaining(self):
        return self._total_cards - self._next_index

    def __str__(self):
        return str(self._cards)


def count_blackjacks(sorter: MultiDeckSorter) -> int:
    blackjacks = 0
    while sorter.remaining():
        card1, card2 = sorter.next_card(), sorter.next_card()
        if (card1[1] == 1 or card2[1] == 1) and (card1[1] > 9 or card2[1] > 9):
            blackjacks += 1
    return blackjacks


def main():
    sorter = MultiDeckSorter(2)
    print(sorter)
    print(f'Remaining = {sorter.remaining()}')
    sorter.reset()
    print(sorter)
    print(f'Remaining = {sorter.remaining()}')

    while card := sorter.next_card():
        print(card)
        print(f'Remain: {sorter.remaining()}')

    sorter.reset()
    print(sorter)
    print(f'Remaining = {sorter.remaining()}')

    sorter = MultiDeckSorter()
    sorter.reset()
    print(f'Black jacks from one sorter = {count_blackjacks(sorter)}')

    num_sorters = 1_000_000
    blackjacks = 0
    for _ in range(num_sorters):
        sorter = MultiDeckSorter()
        sorter.reset()
        blackjacks += count_blackjacks(sorter)
    print(f'Average blackjacks per sorter is {blackjacks/num_sorters}')


if __name__ == '__main__':
    main()
