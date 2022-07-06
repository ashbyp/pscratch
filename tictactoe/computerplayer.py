import random
import time
from tictactoe.player import Player
from tictactoe.game import Game
from tictactoe import utils


class ComputerPlayer(Player):
    def __init__(self, symbol, think=True):
        super().__init__('WOPR', symbol)
        self.think = think

    def stop_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            free = [x for x in win_set if grid[x[0]][x[1]] == Game.BLANK]
            if len(free) == 1:
                not_mine = [x for x in win_set if grid[x[0]][x[1]] not in (Game.BLANK, self.symbol)]
                if len(not_mine) == size - 1:
                    return free.pop()
        return None

    def check_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            free = [x for x in win_set if grid[x[0]][x[1]] == Game.BLANK]
            if len(free) == 1:
                mine = [x for x in win_set if grid[x[0]][x[1]] == self.symbol]
                # there is one free slot, check to see if the others are filled by me
                if len(mine) == size - 1:
                    return free.pop()
        return None

    def choose_potential_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            mine = [x for x in win_set if grid[x[0]][x[1]] == self.symbol]
            if mine:
                free = [x for x in win_set if grid[x[0]][x[1]] == Game.BLANK]
                if len(mine) + len(free) == size and len(free) > 0:
                    return free.pop()
        return None

    @staticmethod
    def choose_random(grid, size):
        return random.choice([(i, j) for i in range(size) for j in range(size)
                              if grid[i][j] == Game.BLANK])

    def enter_coord(self, grid):
        print(f'{self.name} thinking...')
        if self.think:
            time.sleep(1)
        size = len(grid[0])
        grid_ref = self.check_win(grid, size) or self.stop_win(grid, size) \
                   or self.choose_potential_win(grid, size) or self.choose_random(grid, size)
        return grid_ref[0] + 1, grid_ref[1] + 1

    def reenter_coord(self, grid):
        return self.enter_coord(grid)

    def result(self, grid, result):
        pass
