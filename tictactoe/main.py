import random

from tictactoe.game import Game
from tictactoe.humanplayer import HumanPlayer
from tictactoe.computerplayer import ComputerPlayer
from tictactoe.remoteplayer import RemotePlayer


def get_grid_size():
    size = input('Enter grid size: (3)')
    try:
        size = int(size)
    except:
        size = 3
    return size


def run_server():
    size = get_grid_size()
    players = [RemotePlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    while True:
        random.shuffle(players)
        g = Game(players[0], players[1], size)
        g.play()


def run_local():
    size = get_grid_size()
    players = [HumanPlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    while True:
        random.shuffle(players)
        g = Game(players[0], players[1], size)
        g.play()


if __name__ == '__main__':
    run_local()
