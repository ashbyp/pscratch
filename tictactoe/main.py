import random
from threading import Thread
from json.decoder import JSONDecodeError

from tictactoe.game import Game
from tictactoe.humanplayer import HumanPlayer
from tictactoe.computerplayer import ComputerPlayer
from tictactoe.remoteplayer import RemotePlayer
from tictactoe.player import Player


def get_grid_size() -> int:
    size = input('Enter grid size: (3)')
    try:
        size = int(size)
    except ValueError as _:
        size = 3
    return size


def game_thread(players: list[Player], size: int, game_id: int):
    print(f'Starting game {game_id}')
    keep_playing = True
    while keep_playing:
        try:
            random.shuffle(players)
            g = Game(players[0], players[1], size)
            keep_playing = g.play()
        except ConnectionResetError as cre:
            print(f'Connection reset on game {game_id} - {cre}')
            return
        except JSONDecodeError as jde:
            print(f'Message error on game id {game_id} - {jde}')
            return

    print(f'Game id {game_id} ended by opponent')


def run_server() -> None:
    size = get_grid_size()
    game_id = 0

    while True:
        players = [RemotePlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS, think_seconds=0.25)]
        game_id += 1
        game = Thread(target=game_thread, args=(players, size, game_id))
        game.start()


def run_local() -> None:
    size = get_grid_size()
    players = [HumanPlayer(Game.NOUGHT), ComputerPlayer(Game.CROSS)]
    keep_playing = True

    while keep_playing:
        random.shuffle(players)
        g = Game(players[0], players[1], size)
        keep_playing = g.play()


if __name__ == '__main__':
    run_local()
