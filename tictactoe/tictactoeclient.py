import socket
import re
from tictactoe.message import Message
from tictactoe import utils


class TicTacToeClient:

    def __init__(self):
        self.name = input('Enter your name: ')
        self.con, self.symbol = self._get_connection()

    def play(self):
        while True:
            msg = Message.get_next(self.con)
            if msg.code == Message.ENTER_COORD:
                self._process_play_message(msg)
            elif msg.code == Message.REENTER_COORD:
                print(' *** invalid coord, try again')
                self._process_play_message(msg)
            elif msg.code == Message.RESULT:
                self._process_result_message(msg)
            else:
                print('Received invalid message:', msg)
                raise ValueError(msg)

    def _process_play_message(self, msg):
        grid = msg.data['grid']
        utils.print_grid(grid)
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        Message.send(self.con, Message.coord_message(tuple(map(int, re.findall(r'[0-9]+', coord)))))


    def _process_result_message(self, msg):
        grid = msg.data['grid']
        result = msg.data['result']
        utils.print_grid(grid)
        print(f'End of game, result is {result}')

    def _get_connection(self):
        print('Establishing connection to server...')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 65432))
        msg = Message.name_message(self.name)
        msg.send(s, msg)
        msg = Message.get_next(s)
        symbol = msg.data['symbol']
        return s, symbol


if __name__ == '__main__':
    client = TicTacToeClient()
    client.play()