import random

from tictactoe.game import Game
from tictactoe.humanplayer import HumanPlayer
from tictactoe.computerplayer import ComputerPlayer


def main():
    size = input('Enter grid size: (3)')
    try:
        size = int(size)
    except:
        size = 3

    players = [HumanPlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    while True:
        random.shuffle(players)
        g = Game(players[0], players[1], size)
        g.play()


if __name__ == '__main__':
    main()
