


def fill_board(size, value):
    return [[value for _ in range(size)] for _ in range(size)]


class Game:

    NOUGHT = '0'
    CROSS = 'X'
    BLANK = ' '

    def __init__(self, player1, player2, grid_size=3):
        self.player1 = player1
        self.player2 = player2
        self.grid_size = grid_size
        print(f'TicTacToe {self.player1} vs {self.player2}')

        # TODO: allow other grid sizes
        if self.grid_size != 3:
            raise ValueError('only a grid size of 3 is supported')

    def print_grid(self, grid):
        board = """
             |     |   
          %s  |  %s  |  %s
        -----|-----|-----
          %s  |  %s  |  %s
        -----|-----|-----
          %s  |  %s  |  %s
             |     |
        """
        print(board % tuple(grid[i][j] for i in range(self.grid_size) for j in range(self.grid_size)))

    def invalid_play(self, grid, coord):
        if len(coord) != 2:
            return True

        row, col = coord
        if row < 1 or row > self.grid_size or col < 1 or col > self.grid_size:
            return True

        if grid[row-1][col-1] != self.BLANK:
            return True

        return False

    def check_winner(self, grid):
        # rows and cols
        for i in range(self.grid_size):
            if all(grid[i][j] == self.NOUGHT for j in range(self.grid_size)):
                return self.NOUGHT
            if all(grid[i][j] == self.CROSS for j in range(self.grid_size)):
                return self.CROSS
            if all(grid[j][i] == self.NOUGHT for j in range(self.grid_size)):
                return self.NOUGHT
            if all(grid[j][i] == self.CROSS for j in range(self.grid_size)):
                return self.CROSS

        # top-left to bottom-right
        if all(grid[i][i] == self.NOUGHT for i in range(self.grid_size)):
            return self.NOUGHT
        if all(grid[i][i] == self.CROSS for i in range(self.grid_size)):
            return self.CROSS

        # top-right to bottom-left
        if all(grid[i][2-i] == self.NOUGHT for i in range(self.grid_size)):
            return self.NOUGHT
        if all(grid[i][2-i] == self.CROSS for i in range(self.grid_size)):
            return self.CROSS

        return None

    def play(self):
        p1 = self.player1
        p2 = self.player2

        grid = fill_board(self.grid_size, self.BLANK)
        plays = 0
        max_plays = self.grid_size ** 2

        while True:
            self.print_grid(grid)
            coord = p1.play(grid, self.grid_size)
            while self.invalid_play(grid, coord):
                print(f' ** invalid play {coord}')
                coord = p1.play(grid, self.grid_size)

            plays += 1
            print(f'{p1} played {coord}')
            grid[coord[0]-1][coord[1]-1] = p1.symbol

            winning_symbol = self.check_winner(grid)
            if winning_symbol:
                self.print_grid(grid)
                winner = p1.name if winning_symbol == p1.symbol else p2.name
                print(f'{winner} has won!')
                break

            if plays == max_plays:
                self.print_grid(grid)
                print('Game is drawn')
                break

            p1, p2 = p2, p1

        print('Done')

