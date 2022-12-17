import json
from json.decoder import JSONDecodeError
from enum import Enum, auto


class MessageType(Enum):
    SYMBOL = auto()
    ENTER_COORD = auto()
    RESULT = auto()
    NAME = auto()
    COORD = auto()
    REENTER_COORD = auto()
    PLAY_AGAIN = auto()


DEBUG: bool = False


class Message:

    def __init__(self, code: MessageType, data: dict) -> None:
        self.code = code
        self.data = data

    @classmethod
    def symbol_message(cls, symbol: str):
        return cls(MessageType.SYMBOL, dict(symbol=symbol))

    @classmethod
    def enter_coord_message(cls, grid: list[list[str]]):
        return cls(MessageType.ENTER_COORD, dict(grid=grid))

    @classmethod
    def result_message(cls, grid: list[list[str]], result: bool):
        return cls(MessageType.RESULT, dict(grid=grid, result=result))

    @classmethod
    def play_again_message(cls, again:  bool):
        return cls(MessageType.PLAY_AGAIN, dict(again=again))

    @classmethod
    def name_message(cls, name: str):
        return cls(MessageType.NAME, dict(name=name))

    @classmethod
    def coord_message(cls, coord: tuple[int, int]):
        return cls(MessageType.COORD, dict(coord=coord))

    @classmethod
    def reenter_coord_message(cls, grid: list[list[str]]):
        return cls(MessageType.REENTER_COORD, dict(grid=grid))

    @staticmethod
    def get_next(conn):
        raw = conn.recv(1024).decode('utf-8')
        try:
            payload = json.loads(raw)
            if DEBUG:
                print('Received:')
                print(payload)
            code = payload['code']
            data = payload['data']
            return Message(MessageType(code), data)
        except JSONDecodeError as e:
            print(f'Error reading message\n{raw}')
            raise e

    @staticmethod
    def send(conn, message):
        payload = dict(code=message.code.value, data=message.data)
        json_payload = json.dumps(payload)
        if DEBUG:
            print('Sending')
            print(json_payload)
        conn.sendall(bytes(json_payload, 'utf8'))

    def __str__(self):
        return f'Code: {self.code}\nData: {self.data}'
