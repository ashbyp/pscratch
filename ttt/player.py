
class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        print(f'{self.name} is {self.symbol}')

    def play(self, grid, grid_size):
        raise NotImplemented()

    def __str__(self):
        return self.name

