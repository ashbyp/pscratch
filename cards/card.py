import random
import itertools

SUITS = {
    'Club': 0,
    'Diamond': 1,
    'Heart': 2,
    'Spade': 3,
}
SUIT_NAMES = tuple(SUITS.keys())
SHORT_SUITS_MAP = {k[0]: k for k in SUITS.keys()}

PICTURES = {
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 1
}

SHORT_PICTURES = {k[0]: v for k, v in PICTURES.items()}
RANK_TO_PICTURES = {v: k for k, v in PICTURES.items()}


class Card:
    def __init__(self, rank, suit):
        try:
            self._rank = int(rank)
            if self._rank < 0 or self._rank > 13:
                raise ValueError('rank must be between 1-13')
        except ValueError as e:
            raise ValueError("rank must be an integer", e)

        if suit not in SUIT_NAMES:
            raise ValueError(f'suit must be one of {SUIT_NAMES}')
        self._suit = suit
        self._value = self._rank if self._rank < 11 else 10

    @staticmethod
    def from_str(card_name):
        # AD 1D ad 1d  - all ace diamonds
        # 10S 10s - both 10 spades
        # 5C 5c - both 5 clubs
        # JH Jh 11H 11h - all jack of hearts
        card_name = card_name.upper()
        rank_str = card_name[0:2] if len(card_name) == 3 else card_name[0]
        if rank_str in SHORT_PICTURES:
            rank = int(SHORT_PICTURES[rank_str])
        else:
            rank = int(rank_str)

        short_suit_name = card_name[-1]
        if short_suit_name not in SHORT_SUITS_MAP:
            raise ValueError(f'short suit name must be one of {SHORT_SUITS_MAP.keys()}')
        return Card(rank, SHORT_SUITS_MAP[card_name[-1]])

    @staticmethod
    def from_str_list(card_names):
        return [Card.from_str(name) for name in card_names.replace(' ', '').split(',')]

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
        return RANK_TO_PICTURES.get(self._rank, str(self._rank))

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
        return hash(self.__repr__())


class Deck:
    def __init__(self, cards=None):
        self._cards = standard_deck() if not cards else cards

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self, num_players, cards_per_hand):
        dealt = [[] for _ in range(num_players)]
        for i in range(cards_per_hand):
            for j in range(num_players):
                dealt[j].append(self._cards.pop())
        return dealt

    def deal_one(self, num_cards):
        return [self._cards.pop() for _ in range(num_cards)]

    def cards_remaining(self):
        return len(self._cards)

    def next_card(self):
        return self._cards.pop(0)

    def random_card(self):
        card = random.choice(self._cards)
        self._cards.remove(card)
        return card

    def return_card(self, returned):
        self._cards.append(returned)

    def return_cards(self, returned):
        self._cards.extend(returned)


def standard_deck():
    return [Card(r, s) for r in range(1, 14) for s in SUIT_NAMES]


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
    cards = sorted(cards)
    for i in range(0, len(cards) - 1):
        if cards[i].rank != cards[i+1].rank - 1:
            return False
    return True


def any_suit_runs(cards, min_run_size):
    potential = []

    for i in range(min_run_size, len(cards) + 1):
        for comb in itertools.combinations(cards, i):
            if is_run(comb):
                potential.append(set(comb))

    deduped = []
    for s in potential:
        subset = False
        for o in potential:
            if s.issubset(o) and s is not o:
                subset = True
        if not subset:
            deduped.append(list(s))
    return deduped


def flushes(cards, min_flush_size):
    return [c for c in split_suits(cards).values() if len(c) >= min_flush_size]


def pairs(hand):
    return [list(comb) for comb in itertools.combinations(hand, 2) if comb[0].rank == comb[1].rank]

