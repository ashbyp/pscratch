from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol
        print(f'{self.name} is {self.symbol}')
        super().__init__()

    @abstractmethod
    def enter_coord(self, grid):
        """
        Player should return the coordinate of the square they with to play in.  Top-left corner is
        (1, 1) - it's 1 based
        :param grid: square grid populated with 0's, X's and ' 's`
        :return: a tuple identifying the slot to play into
        """
        pass

    @abstractmethod
    def reenter_coord(self, grid):
        """
        Called if the previous call to enter_coord returned and invalid coordinate (out of range for the
        grid or the given square was occupied already.

        Player should return the coordinate of the square they with to play in.  Top-left corner is
        (1, 1) - it's 1 based
        :param grid: square grid populated with 0's, X's and ' 's`
        :return: a tuple identifying the slot to play into
        """
        pass

    @abstractmethod
    def result(self, grid, result):
        """
        Called when the game is finished - return true if you want to play again
        :param grid: the final state of the playing grid
        :param result: A string "win", "lose,"draw"
        :return: bool
        """
        pass

    def __str__(self):
        return self.name
