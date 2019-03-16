from unittest import TestCase

from cards import card
from cards import crib_game
from cards import crib_player


class TestCribGame(TestCase):

    def setUp(self):
        self._player1 = crib_player.DumbComputerPlayer('p1')
        self._player2 = crib_player.DumbComputerPlayer('p2')
        self._game = crib_game.CribGame(self._player1, self._player2, 121, messages_enabled=False, trace_enabled=False)
        self._board = crib_game.CribBoard(self._player1, self._player2, 121)

    def test_CribBoard_constructor(self):
        self.assertEqual(0, self._board.player_score(self._player1))
        self.assertEqual(0, self._board.player_score(self._player2))
        self.assertEqual('p1: 0, p2: 0', str(self._board))

    def test_CribBoard_pegging(self):
        self._board.add_points(self._player1, 10)
        self._board.add_points(self._player1, 12)
        self._board.add_points(self._player2, 3)
        self._board.add_points(self._player2, 2)
        self.assertEqual(22,self._board.player_score(self._player1))
        self.assertEqual(5, self._board.player_score(self._player2))
        self.assertEqual('p1: 22, p2: 5', str(self._board))

    def test_CribBoard_player1_wins(self):
        self._board.add_points(self._player1, 10)
        with self.assertRaises(crib_game.GameWonException):
            self._board.add_points(self._player1, 112)
        self.assertEqual(122, self._board.player_score(self._player1))

    def test_CribBoard_player2_wins(self):
        self._board.add_points(self._player2, 10)
        with self.assertRaises(crib_game.GameWonException):
            self._board.add_points(self._player2, 112)
        self.assertEqual(122, self._board.player_score(self._player2))

    def test_CribGame_decide_dealer(self):
        deck = card.Deck()
        deck.shuffle()
        for _ in range(100):
            dealer, non_dealer, dealer_card, non_dealer_card = self._game.decide_dealer(deck)
            self.assertTrue(dealer_card > non_dealer_card)
            self.assertEqual(52, deck.cards_remaining())

    def test_CribGame_discard(self):
        deck = card.Deck()
        hands = deck.deal(2, 6)
        dealer_hand, non_dealer_hand, box = self._game.discard(self._player1, self._player2, hands[0], hands[1])
        self.assertEqual(4, len(dealer_hand))
        self.assertEqual(4, len(non_dealer_hand))
        self.assertEqual(4, len(box))
        self.assertTrue(all([x not in dealer_hand and x not in non_dealer_hand for x in box]))

    def test_CribGame_turn(self):
        deck = card.Deck()
        turn_card = self._game.turn(deck, self._player1, self._board)
        self.assertTrue(turn_card is not None)
        deck = card.Deck([card.Card('11', 'Heart')])
        turn_card = self._game.turn(deck, self._player1, self._board)
        self.assertEqual(card.Card('11', 'Heart'), turn_card)
        self.assertEqual(2, self._board.player_score(self._player1))

    def test_CribGame_play_pegging_card_empty_stack(self):
        stack = []
        hand = card.Card.from_str_list('QS, JD, 6C, 2H')
        turn = card.Card.from_str('3C')

        go = self._game.play_pegging_card(self._player1, stack, hand, turn, self._board)

        self.assertEqual(1, len(stack))
        self.assertEqual(card.Card.from_str('QS'), stack[0])
        self.assertEqual(0, self._board.player_score(self._player1))
        self.assertFalse(go)

    def test_CribGame_play_pegging_card_15(self):
        stack = card.Card.from_str_list('10C')
        hand = card.Card.from_str_list('5d, JD, 6C, 2H')
        turn = card.Card.from_str('3C')

        go = self._game.play_pegging_card(self._player1, stack, hand, turn, self._board)

        self.assertEqual(2, len(stack))
        self.assertEqual(card.Card.from_str('5d'), stack[1])
        self.assertEqual(2, self._board.player_score(self._player1))
        self.assertFalse(go)

    def test_CribGame_play_pegging_card_31(self):
        stack = card.Card.from_str_list('10C,10D,10S')
        hand = card.Card.from_str_list('AS, JD, 6C, 2H')
        turn = card.Card.from_str('3C')

        self.assertEqual(3, len(stack))

        go = self._game.play_pegging_card(self._player1, stack, hand, turn, self._board)

        self.assertEqual(4, len(stack))
        self.assertEqual(card.Card.from_str('AS'), stack[3])
        self.assertEqual(2, self._board.player_score(self._player1))
        self.assertFalse(go)

    def test_CribGame_play_pegging_card_GO(self):
        stack = card.Card.from_str_list('10C,10D,10S')
        hand = card.Card.from_str_list('JD, 6C, 2H')
        turn = card.Card.from_str('3C')

        self.assertEqual(3, len(stack))

        go = self._game.play_pegging_card(self._player1, stack, hand, turn, self._board)

        self.assertEqual(3, len(stack))
        self.assertEqual(0, self._board.player_score(self._player1))
        self.assertTrue(go)

    def test_CribGame_play_pegging_card_game_won(self):
        self._board.add_points(self._player1, 120)
        stack = card.Card.from_str_list('10C,10D,10S')
        hand = card.Card.from_str_list('AC, 6C, 2H')
        turn = card.Card.from_str('3C')

        with self.assertRaises(crib_game.GameWonException):
            self._game.play_pegging_card(self._player1, stack, hand, turn, self._board)

        self.assertEqual(122, self._board.player_score(self._player1))

    def test_CribGame_pegging_score_31(self):
        dealer = card.Card.from_str_list('AD, 3D, 5D, 7S')
        non_dealer = card.Card.from_str_list('QH, 10H, 7H, 5C')

        self._game.pegging(self._player1, self._player2, dealer, non_dealer, card.Card.from_str('KC'), self._board)

        #  QH, AD, 10H, 3D, 7H = 31 scored by non_dealer 2+1 points
        #  5D 5C 7S = last card for dealer, 1 point

        self.assertEqual(1, self._board.player_score(self._player1))
        self.assertEqual(3, self._board.player_score(self._player2))

    def test_CribGame_pegging_score_15(self):
        dealer = card.Card.from_str_list('5D, 3D, 8D, 7S')
        non_dealer = card.Card.from_str_list('QH, 10H, 7H, 5C')

        self._game.pegging(self._player1, self._player2, dealer, non_dealer, card.Card.from_str('KC'), self._board)

        # QH 5D (dealer scores 2) 10H 3D last card for dealer, dealer total 3 points
        # 7H 8D (dealer scores 2) 5C 7S last card for dealer, dealer total 3 points

        self.assertEqual(6, self._board.player_score(self._player1))
        self.assertEqual(0, self._board.player_score(self._player2))


