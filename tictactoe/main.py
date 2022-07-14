import random
import signal
from threading import Thread
from json.decoder import JSONDecodeError

from tictactoe.game import Game
from tictactoe.humanplayer import HumanPlayer
from tictactoe.computerplayer import ComputerPlayer
from tictactoe.remoteplayer import RemotePlayer


def get_grid_size():
    size = input('Enter grid size: (3)')
    try:
        size = int(size)
    except ValueError as _:
        size = 3
    return size


def game_thread(players, size, game_id):
    print(f'Starting game {game_id}')
    while True:
        try:
            random.shuffle(players)
            g = Game(players[0], players[1], size)
            g.play()
        except ConnectionResetError as cre:
            print(f'Connection reset on game {game_id} - {cre}')
            return
        except JSONDecodeError as jde:
            print(f'Message error on game id {game_id} - {jde}')
            return


def ctrl_c_handler(signum, frame):
    print('Ctrl+C received, exiting')
    exit(0)


def run_server():
    signal.signal(signal.SIGINT, ctrl_c_handler)
    size = get_grid_size()
    game_id = 0

    while True:
        players = [RemotePlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS, think_seconds=0.25)]
        game_id += 1
        game = Thread(target=game_thread, args=(players, size, game_id))
        game.start()


def run_local():
    size = get_grid_size()
    players = [HumanPlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    while True:
        random.shuffle(players)
        g = Game(players[0], players[1], size)
        g.play()


if __name__ == '__main__':
    run_local()
