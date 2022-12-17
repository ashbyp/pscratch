import socket
import re
import time
from tictactoe.message import MessageType, Message
from tictactoe import utils


class TicTacToeClient:

    def __init__(self, host, port, name=None):
        self.name = name or input('Enter your name: ')
        self.conn = self._get_connection(host, port)
        self.symbol = self._handshake()

    def play(self):
        keep_playing = True
        while keep_playing:
            msg = Message.get_next(self.conn)
            if msg.code == MessageType.ENTER_COORD:
                self._process_play_message(msg)
            elif msg.code == MessageType.REENTER_COORD:
                print(' *** invalid coord, try again')
                self._process_play_message(msg)
            elif msg.code == MessageType.RESULT:
                keep_playing = self._process_result_message(msg)
            else:
                print('Received invalid message:', msg)
                raise ValueError(msg)
        self.conn.close()

    def _process_play_message(self, msg):
        grid = msg.data['grid']
        utils.print_grid(grid)
        coord = input(f'{self.name} ({self.symbol}\'s) Enter coord: ')
        Message.send(self.conn, Message.coord_message(tuple(map(int, re.findall(r'[0-9]+', coord)))))

    def _process_result_message(self, msg):
        grid = msg.data['grid']
        result = msg.data['result']
        utils.print_grid(grid)
        print(f'End of game, result is {result}')
        play_again = input('Play again? ([y]/n): ')
        try:
            again = not play_again or play_again.lower().startswith('y')
        except ValueError as _:
            again = False
        Message.send(self.conn, Message.play_again_message(again))
        return again

    @staticmethod
    def _get_connection(host, port):
        print(f'Establishing connection to server {host}:{port} ({socket.gethostbyname(host)})')
        retries = 10
        while retries > 0:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((socket.gethostbyname(host), port))
                return s
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
    client = TicTacToeClient('localhost', 65432, name=None)
    client.play()


if __name__ == '__main__':
    main()
