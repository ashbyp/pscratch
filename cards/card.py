import random
import itertools

SUITS = {
    'Club': 0,
    'Diamond': 1,
    'Heart': 2,
    'Spade': 3,
}
SUIT_NAMES = tuple(SUITS.keys())


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self._value = self._rank if self._rank < 11 else 10

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    @property
    def value(self):
        return self._value

    def str_rank(self):
        return {11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace'}.get(self._rank, str(self._rank))

    def _cmp(self, other):
        if self.rank != other.rank:
            return self.rank - other.rank
        else:
            return SUITS[self.suit] - SUITS[other.suit]

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __ne__(self, other):
        return self._cmp(other) != 0

    def __ge__(self, other):
        return self._cmp(other) >= 0

    def __gt__(self, other):
        return self._cmp(other) > 0

    def __repr__(self):
        return '{0} of {1}s'.format(self.str_rank(), self._suit)

    def __str__(self):
        return '{0} of {1}s'.format(self.str_rank(), self._suit)

    def __hash__(self):
        return id(self)


class Deck:
    def __init__(self):
        self._cards = standard_deck()

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, num_players, cards_per_hand):
        dealt = [[] for _ in range(num_players)]
        for i in range(cards_per_hand):
            for j in range(num_players):
                dealt[j].append(self._cards.pop())
        return dealt

    def cards_remaining(self):
        return len(self._cards)

    def next_card(self):
        return self._cards.pop()

    def return_cards(self, returned):
        self._cards.extend(returned)


def standard_deck():
    return [Card(s, v) for s in SUIT_NAMES for v in range(1, 14)]


def split_suits(cards):
    split = {}
    for suit in SUIT_NAMES:
        split[suit] = sorted([c for c in cards if c.suit == suit])
    return split


def split_ranks(cards):
    split = {}
    for c in cards:
        split[c.rank] = split.get(c.rank, [])
        split[c.rank].append(c)
    return split


def same_suit_runs(cards, min_run_size):
    results = []
    for suit, cards_for_suit in split_suits(cards).items():
        run_for_suit = []
        for c in cards_for_suit:
            if len(run_for_suit) == 0 or run_for_suit[len(run_for_suit) - 1].rank == c.rank - 1:
                run_for_suit.append(c)
        if len(run_for_suit) >= min_run_size:
            results.append(run_for_suit)
    return results


def is_run(cards):
    for i in range(0, len(cards) - 1):
        if cards[i].rank != cards[i+1].rank - 1:
            return False
    return True


def any_suit_runs(cards, min_run_size):
    results = []

    def find(run_size):
        for comb in itertools.combinations(cards, run_size):
            s = sorted(comb)
            if is_run(s):
                results.append(list(s))

    for i in range(min_run_size, len(cards) + 1):
        find(i)

    return results


def flushes(cards, min_flush_size):
    return [c for c in split_suits(cards).values() if len(c) >= min_flush_size]


def pairs(hand):
    return [list(comb) for comb in itertools.combinations(hand, 2) if comb[0].rank == comb[1].rank]


if __name__ == '__main__':
    h = [
        Card('S', 3),
        Card('H', 3),
        Card('D', 3)
    ]

