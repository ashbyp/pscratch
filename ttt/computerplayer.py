import random, time
from ttt.player import Player
from ttt.game import Game
from ttt import utils


class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__('WOPPER', symbol)

    def stop_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            free = {x for x in win_set if grid[x[0]][x[1]] == Game.BLANK}
            if len(free) == 1:
                not_mine = {x for x in win_set if grid[x[0]][x[1]] not in (Game.BLANK, self.symbol)}
                if len(not_mine) == size - 1:
                    return free.pop()

        return None

    def check_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            free = {x for x in win_set if grid[x[0]][x[1]] == Game.BLANK}
            if len(free) == 1:
                mine = {x for x in win_set if grid[x[0]][x[1]] == self.symbol}
                # there is one free slot, check to see if the others are filled by me
                if len(mine) == size - 1:
                    return free.pop()
        return None

    def choose_potential_win(self, grid, size):
        for win_set in utils.get_line_sets(size):
            mine = {x for x in win_set if grid[x[0]][x[1]] == self.symbol}
            if mine:
                free = {x for x in win_set if grid[x[0]][x[1]] == Game.BLANK}
                if len(mine) + len(free) == size and len(free) > 0:
                    return free.pop()
        return None

    @staticmethod
    def choose_random(grid, size):
        return random.choice([(i, j) for i in range(size) for j in range(size)
                              if grid[i][j] == Game.BLANK])

    def play(self, grid, size):
        print(f'{self.name} thinking...')
        time.sleep(1)
        grid_ref = self.stop_win(grid, size) or self.check_win(grid, size) \
                    or self.choose_potential_win(grid, size) or self.choose_random(grid, size)
        return grid_ref[0] + 1, grid_ref[1] + 1


