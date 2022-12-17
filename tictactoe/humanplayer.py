import re
from builtins import ValueError

from tictactoe.player import Player


class HumanPlayer(Player):
    def __init__(self, symbol: str) -> None:
        super().__init__(input('Enter your name: '), symbol)

    def enter_coord(self, grid: list[list[str]]) -> tuple[int, ...]:
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        return tuple(map(int, re.findall(r'[0-9]+', coord)))

    def reenter_coord(self, grid: list[list[str]]) -> tuple[int, ...]:
        return self.enter_coord(grid)

    def result(self, grid: list[list[str]], result: bool) -> bool:
        play_again = input('Play again? ([y]/n): ')
        try:
            return not play_again or play_again.lower().startswith('y')
        except ValueError as _:
            return False
