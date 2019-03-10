from unittest import TestCase

from cards import crib_game


class TestCribGame(TestCase):

    def setUp(self):
        self._player1 = crib_game.DumbComputerPlayer('paul')
        self._player2 = crib_game.DumbComputerPlayer('test')

    def test_CribBoardConstructor(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        self.assertEqual(0, board.player1_score)
        self.assertEqual(0, board.player2_score)
        self.assertEqual('paul: 0, test: 0', str(board))

    def test_CribBoardPegging(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_player1_points(10)
        board.add_player1_points(12)
        board.add_player2_points(3)
        board.add_player2_points(2)
        self.assertEqual(22, board.player1_score)
        self.assertEqual(5, board.player2_score)
        self.assertEqual('paul: 22, test: 5', str(board))

    def test_CribBoardPlayer1Wins(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_player1_points(10)
        with self.assertRaises(crib_game.GameWonException):
            board.add_player1_points(112)
        self.assertEqual(122, board.player1_score)

    def test_CribBoardPlayer2Wins(self):
        board = crib_game.CribBoard(self._player1, self._player2, 121)
        board.add_player2_points(10)
        with self.assertRaises(crib_game.GameWonException):
            board.add_player2_points(112)
        self.assertEqual(122, board.player2_score)