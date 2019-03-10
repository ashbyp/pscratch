from cards import card


class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0

    @property
    def name(self):
        return self._name

    def choose_discards(self, hand):
        raise NotImplementedError()


class DumbComputerPlayer(Player):
    ME_COUNT = 1

    def __init__(self, name=None):
        if not name:
            Player.__init__(self, f'Computer ({DumbComputerPlayer.ME_COUNT})')
            DumbComputerPlayer.ME_COUNT += 1
        else:
            Player.__init__(self, name)

    def choose_discards(self, hand):
        return hand[0:2]


class HumanPlayer(DumbComputerPlayer): # for now
    pass


class GameWonException(Exception):
    def __init__(self, winning_player, winning_player_score):
        super().__init__(f'{winning_player.name} won with {winning_player_score}')
        self._winning_player = winning_player


class CribBoard:

    def __init__(self, player1, player2, target_points):
        self._player1 = player1
        self._player2 = player2
        self._target_points = target_points
        self._p1_front_peg = 0
        self._p1_back_peg = 0
        self._p2_front_peg = 0
        self._p2_back_peg = 0

    def add_player1_points(self, points):
        self._p1_back_peg = self._p1_front_peg
        self._p1_front_peg += points
        if self._p1_front_peg >= self._target_points:
            raise GameWonException(self._player1, self._p1_front_peg)

    def add_player2_points(self, points):
        self._p2_back_peg = self._p2_front_peg
        self._p2_front_peg += points
        if self._p2_front_peg >= self._target_points:
            raise GameWonException(self._player2, self._p2_front_peg)

    @property
    def player1_score(self):
        return self._p1_front_peg

    @property
    def player2_score(self):
        return self._p2_front_peg

    def __str__(self):
        return f'{self._player1.name}: {self.player1_score}, {self._player2.name}: {self.player2_score}'


class CribGame:

    def __init__(self, player1, player2, target_score, trace_enabled=False):
        self._trace_enabled = trace_enabled
        self._player1 = player1
        self._player2 = player2
        self._target_score = target_score
        self._welcome()

    def _welcome(self):
        print(' ************************************************ ')
        print(f'     Welcome to Cribbage v0.1')
        print(f'      {self._player1.name}')
        print(f'      {self._player1.name}')
        print(' ************************************************ ')

    def _announce_win(self, message, board):
        print(' ************************************************ ')
        print(f'     Winner                                      ')
        print(f'      {message}                                  ')
        print(' ************************************************ ')

    def _trace(self, msg):
        if self._trace_enabled:
            print(msg)

    def play(self):
        deck = card.Deck()
        board = CribBoard(self._player1, self._player2, 121)

        while True:
            try:
                hands = deck.deal(2, 6)

                self._trace(f'{self._player1.name} has been dealt {hands[0]}')
                self._trace(f'{self._player2.name} has been dealt {hands[1]}')

                p1_discards = self._player1.choose_discards(hands[0])
                p2_discards = self._player1.choose_discards(hands[1])

                box = p1_discards + p2_discards

                hands[0] = list(set(hands[0]).difference(set(p1_discards)))
                hands[1] = list(set(hands[0]).difference(set(p1_discards)))

                self._trace(f'{self._player1.name} now has {hands[0]}')
                self._trace(f'{self._player2.name} now has {hands[1]}')
                self._trace(f'Box is {box}')

                board.add_player1_points(122)

            except GameWonException as gwe:
                self._announce_win(str(gwe), board)
                break


if __name__ == '__main__':
    p1 = DumbComputerPlayer()
    p2 = DumbComputerPlayer()

    game = CribGame(p1, p2, 121, trace_enabled=True)
    game.play()









