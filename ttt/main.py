import random

from ttt.game import Game
from ttt.humanplayer import HumanPlayer
from ttt.computerplayer import ComputerPlayer


def main():
    players = [HumanPlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    random.shuffle(players)
    g = Game(players[0], players[1])
    g.play()


if __name__ == '__main__':
    main()
