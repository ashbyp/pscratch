import json
from json.decoder import JSONDecodeError


class Message:
    SYMBOL = 1
    ENTER_COORD = 2
    RESULT = 3
    NAME = 4
    COORD = 5
    REENTER_COORD = 6

    def __init__(self, code, data):
        self.code = code
        self.data = data

    @classmethod
    def symbol_message(cls, symbol):
        return cls(Message.SYMBOL, dict(symbol=symbol))

    @classmethod
    def enter_coord_message(cls, grid):
        return cls(Message.ENTER_COORD, dict(grid=grid))

    @classmethod
    def result_message(cls, grid, result):
        return cls(Message.RESULT, dict(grid=grid, result=result))

    @classmethod
    def name_message(cls, name):
        return cls(Message.NAME, dict(name=name))

    @classmethod
    def coord_message(cls, coord):
        return cls(Message.COORD, dict(coord=coord))

    @classmethod
    def reenter_coord_message(cls, grid):
        return cls(Message.REENTER_COORD, dict(grid=grid))

    @classmethod
    def get_next(cls, conn):
        raw = conn.recv(1024).decode('utf-8')
        try:
            payload = json.loads(raw)
            code = payload['code']
            data = payload['data']
            return Message(code, data)
        except JSONDecodeError as e:
            print(f'Error reading message\n{raw}')
            raise e

    @classmethod
    def send(cls, conn, message):
        payload = dict(code=message.code, data=message.data)
        conn.sendall(bytes(json.dumps(payload), 'utf8'))

    def __str__(self):
        return f'Code: {self.code}\nData: {self.data}'
