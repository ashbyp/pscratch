from tictactoe import utils
from player import Player


class Game:

    WIN: str = "win"
    LOSE: str = "lose"
    DRAW: str = "draw"
    NOUGHT: str = '0'
    CROSS: str = 'X'
    BLANK: str = ' '

    def __init__(self, player1: Player, player2: Player, grid_size: int = 3) -> None:
        if player1.symbol == player2.symbol:
            raise ValueError('players must have different symbols')

        self.player1 = player1
        self.player2 = player2
        self.grid_size = grid_size
        print(f'TicTacToe {self.player1} vs {self.player2}')

    def invalid_play(self, grid: list[list[str]], coord: tuple[int, int]) -> bool:
        if len(coord) != 2:
            return True

        row, col = coord
        if row < 1 or row > self.grid_size or col < 1 or col > self.grid_size:
            return True

        if grid[row-1][col-1] != self.BLANK:
            return True

        return False

    def check_winner(self, grid: list[list[str]]) -> str | None:
        for win_set in utils.get_win_lines(self.grid_size):
            if all(grid[x[0]][x[1]] == Game.NOUGHT for x in win_set):
                return Game.NOUGHT
            if all(grid[x[0]][x[1]] == Game.CROSS for x in win_set):
                return Game.CROSS
        return None

    def play(self) -> bool:
        p1 = self.player1
        p2 = self.player2

        grid = utils.init_grid(self.grid_size, self.BLANK)
        plays = 0
        max_plays = self.grid_size ** 2

        while True:
            utils.print_grid(grid)
            coord = p1.enter_coord(grid)
            while self.invalid_play(grid, coord):
                print(f' ** invalid play {coord}')
                coord = p1.reenter_coord(grid)

            plays += 1
            print(f'{p1} played {coord}')
            grid[coord[0]-1][coord[1]-1] = p1.symbol

            winning_symbol = self.check_winner(grid)
            if winning_symbol:
                utils.print_grid(grid)
                print(f'{p1.name} has won!')
                return p1.result(grid, self.WIN) and p2.result(grid, self.LOSE)

            if plays == max_plays:
                utils.print_grid(grid)
                print('Game is drawn')
                return p1.result(grid, self.DRAW) and p2.result(grid, self.DRAW)

            p1, p2 = p2, p1
