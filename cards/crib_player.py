class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    def choose_discards(self, hand):
        raise NotImplementedError()

    def next_pegging_card(stack, hand, turn_card):#
        raise NotImplementedError()


class DumbComputerPlayer(Player):
    ME_COUNT = 1

    def __init__(self, name=None):
        if not name:
            Player.__init__(self, f'Dumb{DumbComputerPlayer.ME_COUNT}')
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


class HumanPlayer(DumbComputerPlayer):  # for now
    pass
