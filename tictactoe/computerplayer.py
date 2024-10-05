import random
import time
from tictactoe.player import Player
from tictactoe.game import Game
from tictactoe import utils


class ComputerPlayer(Player):
    def __init__(self, symbol: str, think_seconds: float = 1.0):
        super().__init__('WOPR', symbol)
        self.think_seconds = think_seconds

    def stop_win(self, grid: list[list[str]], size: int) -> tuple[int, int] | None:
        for win_line in utils.get_win_lines(size):
            free = [x for x in win_line if grid[x[0]][x[1]] == Game.BLANK]
            if len(free) == 1:
                not_mine = [x for x in win_line if grid[x[0]][x[1]] not in (Game.BLANK, self.symbol)]
                if len(not_mine) == size - 1:
                    return free[0]
        return None

    def check_win(self, grid: list[list[str]], size: int) -> tuple[int, int] | None:
        for win_line in utils.get_win_lines(size):
            free = [x for x in win_line if grid[x[0]][x[1]] == Game.BLANK]
            if len(free) == 1:
                mine = [x for x in win_line if grid[x[0]][x[1]] == self.symbol]
                # there is one free slot, check to see if the others are filled by me
                if len(mine) == size - 1:
                    return free[0]
        return None


    def choose_potential_win(self, grid: list[list[str]], size: int) -> tuple[int, int] | None:
        for win_line in utils.get_win_lines(size):
            mine = [x for x in win_line if grid[x[0]][x[1]] == self.symbol]
            if mine:
                free = [x for x in win_line if grid[x[0]][x[1]] == Game.BLANK]
                if len(mine) + len(free) == size and len(free) > 0:
                    return random.choice(free)
        return None

    @staticmethod
    def choose_random(grid: list[list[str]], size: int) -> tuple[int, int]:
        return random.choice([(i, j) for i in range(size) for j in range(size)
                              if grid[i][j] == Game.BLANK])

    def enter_coord(self, grid: list[list[str]]) -> tuple[int, int]:
        print(f'{self.name} thinking...')
        if self.think_seconds:
            time.sleep(self.think_seconds)
        size = len(grid[0])

        grid_ref = self.check_win(grid, size) or \
            self.stop_win(grid, size) or \
            self.choose_potential_win(grid, size) or \
            self.choose_random(grid, size)

        return grid_ref[0] + 1, grid_ref[1] + 1

    def reenter_coord(self, grid: list[list[str]]) -> tuple[int, int]:
        return self.enter_coord(grid)

    def result(self, grid: list[list[str]], result: bool) -> bool:
        return True
