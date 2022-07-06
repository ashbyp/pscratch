from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        print(f'{self.name} is {self.symbol}')
        super().__init__()

    @abstractmethod
    def enter_coord(self, grid):
        pass

    @abstractmethod
    def reenter_coord(self, grid):
        pass

    @abstractmethod
    def result(self, grid, result):
        pass

    def __str__(self):
        return self.name

