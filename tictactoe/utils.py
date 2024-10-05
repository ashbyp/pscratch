from functools import cache


@cache
def get_win_lines(size: int) -> list[list[tuple[int, int]]]:
    all_lines = []
    all_lines += [[(row, col) for col in range(size)] for row in range(size)]
    all_lines += [[(col, row) for col in range(size)] for row in range(size)]
    all_lines += [[(c, c) for c in range(size)]]
    all_lines += [[(c, size - 1 - c) for c in range(size)]]

    return all_lines


def init_grid(size: int, value: str) -> list[list[str]]:
    return [[value for _ in range(size)] for _ in range(size)]


def print_grid(grid: list[list[str]]):
    grid_size = len(grid[0])
    b = "\n"
    for row in range(grid_size):
        for col in range(grid_size):
            if col == grid_size - 1:
                b += '  %s  \n'
            else:
                b += '  %s  |'
        if row != grid_size - 1:
            for col in range(grid_size):
                if col == grid_size - 1:
                    b += '------\n'
                else:
                    b += '-----|'

    print(b % tuple(grid[i][j] for i in range(grid_size) for j in range(grid_size)))
