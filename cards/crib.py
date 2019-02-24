from cards import card
import itertools


def runs(hand, turn_card):
    return card.any_suit_runs(hand + [turn_card], 3)


def flushes(hand, turn_card):
    if card.flushes(hand, 4):
        x = card.flushes(hand + [turn_card], 4)
        return card.flushes(hand + [turn_card], 4)
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


def break_down(hand, turn_card):
    return {
        'runs': runs(hand, turn_card),
        'flushes': flushes(hand, turn_card),
        'fifteens': fifteens(hand, turn_card),
        'pairs': pairs(hand, turn_card),
        'nob': nob(hand, turn_card)
    }


def score_breakdown(bd):
    score = sum(len(r) for r in bd['runs'])
    score += sum(len(f) for f in bd['flushes'])
    score += len(bd['fifteens']) * 2
    score += len(bd['pairs']) * 2
    if bd['nob']:
        score += 1
    return score


def score_hand(hand, turn_card):
    return score_breakdown(break_down(hand, turn_card))


def score_hand_with_breakdown(hand, turn_card):
    bd = break_down(hand, turn_card)
    return score_breakdown(bd), bd


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


