from cards import card


class Player:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class HumanPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)


class ComputerPlayer(Player):
    COMP_PLAYER = 1

    def __init__(self):
        Player.__init__(self, f'Computer ({ComputerPlayer.COMP_PLAYER})')
        ComputerPlayer.COMP_PLAYER += 1


class CribGame:

    def __init__(self, players):
        self._players = players
        self._num_players = len(self._players)
        self._deck = card.Deck()
        self._scores = [0] * self._num_players

        print(' **************************** ')
        print(f' Welcome to Cribbage {len(players)} players')
        for p in players:
            print(f'    {p.name}')
        print(' **************************** ')

    def play(self):
        self._deck.shuffle()

        hands = self._deck.deal(self._num_players, 6)

        for p in self._players:
            p


if __name__ == '__main__':
    ps = [
        ComputerPlayer(),
        ComputerPlayer()
    ]

    game = CribGame(ps)
    game.play()
