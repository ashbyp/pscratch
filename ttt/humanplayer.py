import re
from ttt.player import Player


class HumanPlayer(Player):
    def __init__(self, symbol=None):
        super().__init__(input('Enter your name: '), symbol=symbol)

    def play(self, grid, grid_size):
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        return tuple(map(int, re.findall(r'[0-9]+', coord)))


