from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        print(f'{self.name} is {self.symbol}')
        super().__init__()

    @abstractmethod
    def play(self, grid, size):
        pass

    def __str__(self):
        return self.name

