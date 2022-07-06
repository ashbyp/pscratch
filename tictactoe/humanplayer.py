import re
from tictactoe.player import Player


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(input('Enter your name: '), symbol)

    def enter_coord(self, grid):
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        return tuple(map(int, re.findall(r'[0-9]+', coord)))

    def reenter_coord(self, grid):
        return self.enter_coord(grid)

    def result(self, grid, result):
        pass
