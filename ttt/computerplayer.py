import random, time
from ttt.player import Player
from ttt.game import Game


class ComputerPlayer(Player):
    def __init__(self, symbol=None):
        super().__init__('WOPPER', symbol=symbol)

    def play(self, grid, grid_size):
        print(f'{self.name} thinking...')
        time.sleep(1)
        # random choice
        open_slots = []
        for i in range(grid_size):
            for j in range(grid_size):
                if grid[i][j] == Game.BLANK:
                    open_slots.append((i+1, j+1))
        return random.choice(open_slots)



