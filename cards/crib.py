from cards import card
import itertools


def runs(hand, turn_card):
    # TODO: does not work, include  3,4,5 and 3,4,5,6 as different runs
    return card.any_suit_runs(hand + [turn_card], 3)


def flushes(hand, turn_card):
    if card.flushes(hand, 4):
        return card.flushes(hand + [turn_card], 5)
    return []


def fifteens(hand, turn_card):
    results = []

    def find(num_cards):
        for comb in itertools.combinations(hand + [turn_card], num_cards):
            if sum(c.value for c in comb) == 15:
                results.append(list(comb))

    for i in range(2, len(hand) + 2):
        find(i)
    return results


def pairs(hand, turn_card):
    return card.pairs(hand + [turn_card])


def nob(hand, turn_card):
    for c in hand:
        if c.rank == 11 and c.suit == turn_card.suit:
            return True
    return False


def score_hand(hand, turn_card):
    score = sum(len(r) for r in runs(hand, turn_card))
    score += sum(len(f) for f in flushes(hand, turn_card))
    score += len(fifteens(hand, turn_card)) * 2
    score += len(pairs(hand, turn_card)) * 2
    if nob(hand, turn_card):
        score += 1
    return score


if __name__ == '__main__':
    d = card.Deck()
    for idx in range(100):
        d.shuffle()
        print('*'*70)
        hands = d.deal(1, 4)
        turn = d.next_card()

        print(f'Hand:        {hands[0]}')
        print(f'Turn:        {turn}')
        print(f' Runs:       {runs(hands[0], turn)}')
        print(f' Flushes:    {flushes(hands[0], turn)}')
        print(f' 15s:        {fifteens(hands[0], turn)}')
        print(f' Pairs:      {pairs(hands[0], turn)}')
        print(f' Nob  :      {nob(hands[0], turn)}')
        print(f' Score:      {score_hand(hands[0], turn)}')
        d.return_cards(*hands)
        d.return_cards([turn])
        print(f'Card remaining: {d.cards_remaining()}')


