import socket

from tictactoe.message import Message
from tictactoe.player import Player


class RemotePlayer(Player):
    """
    Runs on the server, communicates with tictactoeclient
    """
    def __init__(self, symbol):
        self.conn, name = self._wait_for_remote_player(symbol)
        super().__init__(name, symbol)

    def enter_coord(self, grid):
        Message.send(self.conn, Message.enter_coord_message(grid))
        msg = Message.get_next(self.conn)
        return msg.data['coord']

    def result(self, grid, result):
        Message.send(self.conn, Message.result_message(grid, result))
        msg = Message.get_next(self.conn)
        return msg.data['again']

    def reenter_coord(self, grid):
        Message.send(self.conn, Message.reenter_coord_message(grid))
        msg = Message.get_next(self.conn)
        return msg.data['coord']

    @staticmethod
    def _wait_for_remote_player(symbol):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 65432))
            print('Waiting for player to connect')
            s.listen()
            conn, address = s.accept()
            print('Connected by', address)
            msg = Message.get_next(conn)
            name = msg.data['name']
            Message.send(conn, Message.symbol_message(symbol))
            return conn, name
