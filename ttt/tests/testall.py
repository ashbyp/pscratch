from unittest import TestCase
from ttt.player import Player
from ttt.game import Game


class DummyPlayer(Player):

    def play(self, grid, grid_size):
        return None


class TestTicTacToe(TestCase):

    def test_check_winner_size_3(self):
        game = Game(DummyPlayer(), DummyPlayer, 3)




