import socket
import re
import time
from tictactoe.message import Message
from tictactoe import utils


class TicTacToeClient:

    def __init__(self, host, port, name=None):
        self.name = name or input('Enter your name: ')
        self.conn = self._get_connection(host, port)
        self.symbol = self._handshake()

    def play(self):
        while True:
            msg = Message.get_next(self.conn)
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
        Message.send(self.conn, Message.coord_message(tuple(map(int, re.findall(r'[0-9]+', coord)))))

    @staticmethod
    def _process_result_message(msg):
        grid = msg.data['grid']
        result = msg.data['result']
        utils.print_grid(grid)
        print(f'End of game, result is {result}')

    @staticmethod
    def _get_connection(host, port):
        print(f'Establishing connection to server {host}:{port} ({socket.gethostbyname(host)})')
        retries = 10
        while retries > 0:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((socket.gethostbyname(host), port))
                return 10
            except ConnectionRefusedError as _:
                retries -= 1
                print(f'Server not found {retries} retries remaining')
                time.sleep(2)
        raise ConnectionRefusedError('no server found')

    def _handshake(self):
        msg = Message.name_message(self.name)
        msg.send(self.conn, msg)
        msg = Message.get_next(self.conn)
        return msg.data['symbol']


def main():
    client = TicTacToeClient('localhost', 65432, name='paul')
    client.play()


if __name__ == '__main__':
    main()
