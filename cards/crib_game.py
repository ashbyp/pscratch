from cards import card


class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def add_to_score(self, points):
        self._score += points

    def choose_discards(self, hand):
        raise NotImplementedError()


class HumanPlayer(Player):

    def __init__(self, name):
        Player.__init__(self, name)


class ComputerPlayer(Player):
    COMP_PLAYER = 1

    def __init__(self):
        Player.__init__(self, f'Computer ({ComputerPlayer.COMP_PLAYER})')
        ComputerPlayer.COMP_PLAYER += 1


class CribGame:

    def __init__(self, players, target_score):
        self._players = players
        self._num_players = len(self._players)

        if self._num_players != 2:
            raise ValueError('2 player cribbage only')

        self._target_score = target_score

        print(' **************************** ')
        print(f' Welcome to Cribbage {len(players)} players')
        for p in players:
            print(f'    {p.name}')
        print(' **************************** ')

    def _check_win(self):
        for player in self._players:
            if player.score >= self._target_score:
                return player
        return None

    def play(self):
        deck = card.Deck()
        deck.shuffle()

if __name__ == '__main__':
    ps = [
        ComputerPlayer(),
        ComputerPlayer()
    ]

    game = CribGame(ps, 121)
    game.play()









