import random
from cards.base.card import Card
from cards.cribbage import score


class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    def choose_discards(self, hand):
        raise NotImplementedError()

    def next_pegging_card(self, stack, hand, turn_card):
        raise NotImplementedError()


class DumbComputerPlayer(Player):
    # don't change the stupidity of this player, unit tests need it
    ME_COUNT = 1

    def __init__(self, name=None):
        if not name:
            Player.__init__(self, f'Dumb_{DumbComputerPlayer.ME_COUNT}')
            DumbComputerPlayer.ME_COUNT += 1
        else:
            Player.__init__(self, name)

    def choose_discards(self, hand):
        return hand[0:2]

    def next_pegging_card(self, stack, hand, turn_card):  #
        stack_score = sum([x.value for x in stack])
        for card in hand:
            if stack_score + card.value <= 31:
                return card
        return None


class RandomComputerPlayer(Player):
    ME_COUNT = 1

    def __init__(self, name=None):
        if not name:
            Player.__init__(self, f'Random_{DumbComputerPlayer.ME_COUNT}')
            RandomComputerPlayer.ME_COUNT += 1
        else:
            Player.__init__(self, name)

    def choose_discards(self, hand):
        return random.sample(hand, 2)

    def next_pegging_card(self, stack, hand, turn_card):  #
        stack_score = sum([x.value for x in stack])
        random.shuffle(hand)
        for card in hand:
            if stack_score + card.value <= 31:
                return card
        return None


class ComputerPlayerV1(Player):
    ME_COUNT = 1

    def __init__(self, name=None):
        if not name:
            Player.__init__(self, f'CompV1_{ComputerPlayerV1.ME_COUNT}')
            ComputerPlayerV1.ME_COUNT += 1
        else:
            Player.__init__(self, name)

    def choose_discards(self, hand):
        best = score.choose_best_hand(hand, 4)[0][1]
        return [x for x in hand if x not in best]

    def next_pegging_card(self, stack, hand, turn_card):
        stack_score = sum([x.value for x in stack])
        score_per_card = []
        for card in hand:
            if stack_score + card.value <= 31:
                score_per_card.append(score.score_pegging_stack(stack + [card])[0])
            else:
                score_per_card.append(None)

        if all(x is None for x in score_per_card):
            return None

        best_score = max(x for x in score_per_card if x is not None)

        for i, s in enumerate(score_per_card):
            if s == best_score:
                return hand[i]

        return None


class HumanPlayer(DumbComputerPlayer):  # for now
    def __init__(self):
        name = input('What is your name? ')
        Player.__init__(self, name)

    def choose_discards(self, hand):
        print(f'\nYour dealt cards are: {hand}')
        while True:
            try:
                user_input = None
                while not user_input:
                    user_input = input('\nWhat will you discard? ')
                cards = Card.from_str_list(user_input)
                if set(cards).issubset(set(hand)):
                    if len(set(cards)) == 2:
                        return cards
                    else:
                        print('Select two cards please, try again')
                else:
                    print('Please select valid cards from your hand, try again')
            except ValueError as e:
                print(f'Input error "{e}"')

    def next_pegging_card(self, stack, hand, turn_card):
        if not hand:
            return None
        print(f'\nYour hand is {hand}')
        stack_total = sum([x.value for x in stack])
        go_allowed = (min([x.value for x in hand]) + stack_total) > 31
        while True:
            try:
                user_input = input('\nWhat will you peg next (return for GO)? ')
                if not user_input:
                    if go_allowed:
                        return None
                    else:
                        print('GO not allowed, you can play')
                        continue
                card = Card.from_str(user_input)
                if card in hand:
                    if (card.value + stack_total) > 31:
                        print('Total would be more than 31, try again')
                    else:
                        return card
                else:
                    print('Selection is not a subset of your cards, try again')
            except ValueError as e:
                print(f'Input error "{e}"')
