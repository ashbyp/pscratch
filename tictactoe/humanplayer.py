import re
from tictactoe.player import Player


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(input('Enter your name: '), symbol)

    def play(self, grid, size):
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        return tuple(map(int, re.findall(r'[0-9]+', coord)))



