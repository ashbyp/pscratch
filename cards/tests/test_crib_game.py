from unittest import TestCase

from cards import card
from cards import crib_game
from cards import crib_player


class TestCribGame(TestCase):

    def setUp(self):
        self._player1 = crib_player.DumbComputerPlayer('paul')
        self._player2 = crib_player.DumbComputerPlayer('test')

    def test_CribBoard_constructor(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        self.assertEqual(0, board.player_score(self._player1))
        self.assertEqual(0, board.player_score(self._player2))
        self.assertEqual('paul: 0, test: 0', str(board))

    def test_CribBoard_pegging(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_points(self._player1, 10)
        board.add_points(self._player1, 12)
        board.add_points(self._player2, 3)
        board.add_points(self._player2, 2)
        self.assertEqual(22, board.player_score(self._player1))
        self.assertEqual(5, board.player_score(self._player2))
        self.assertEqual('paul: 22, test: 5', str(board))

    def test_CribBoard_player1_wins(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_points(self._player1, 10)
        with self.assertRaises(crib_game.GameWonException):
            board.add_points(self._player1, 112)
        self.assertEqual(122, board.player_score(self._player1))

    def test_CribBoard_player2_wins(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_points(self._player2, 10)
        with self.assertRaises(crib_game.GameWonException):
            board.add_points(self._player2, 112)
        self.assertEqual(122, board.player_score(self._player2))

    def test_CribGame_decide_dealer(self):
        game = crib_game.CribGame(self._player1, self._player2, 121)
        deck = card.Deck()
        deck.shuffle()
        for _ in range(100):
            dealer, non_dealer, dealer_card, non_dealer_card = game.decide_dealer(deck)
            self.assertTrue(dealer_card > non_dealer_card)
            self.assertEqual(52, deck.cards_remaining())

    def test_CribGame_discard(self):
        game = crib_game.CribGame(self._player1, self._player2, 121)
        deck = card.Deck()
        hands = deck.deal(2, 6)
        dealer_hand, non_dealer_hand, box = game.discard(self._player1, self._player2, hands[0], hands[1])
        self.assertEqual(4, len(dealer_hand))
        self.assertEqual(4, len(non_dealer_hand))
        self.assertEqual(4, len(box))
        self.assertTrue(all([x not in dealer_hand and x not in non_dealer_hand for x in box]))

    def test_CribGame_turn(self):
        game = crib_game.CribGame(self._player1, self._player2, 121)
        deck = card.Deck()
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        turn_card = game.turn(deck, self._player1, board)
        self.assertTrue(turn_card is not None)
        deck = card.Deck([card.Card('11', 'Heart')])
        turn_card = game.turn(deck, self._player1, board)
        self.assertEqual(card.Card('11', 'Heart'), turn_card)
        self.assertEqual(2, board.player_score(self._player1))