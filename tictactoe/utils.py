from functools import cache


@cache
def get_win_lines(size: int) -> list[list[tuple[int, int]]]:
    all_lines = []

    for row in range(size):
        row_line = []
        for col in range(size):
            row_line.append((row, col))
        all_lines.append(row_line)

    for col in range(size):
        col_line = []
        for row in range(size):
            col_line.append((row, col))
        all_lines.append(col_line)

    diagonal = []
    for row_col in range(size):
        diagonal.append((row_col, row_col))
    all_lines.append(diagonal)

    diagonal = []
    for row_col in range(size):
        diagonal.append((row_col, size - 1 - row_col))
    all_lines.append(diagonal)

    return all_lines


def get_win_lines_generator(size: int) -> list[list[tuple[int, int]]]:
    for row in range(size):
        row_line = []
        for col in range(size):
            row_line.append((row, col))
        yield row_line

    for col in range(size):
        col_line = []
        for row in range(size):
            col_line.append((row, col))
        yield col_line

    diagonal = []
    for row_col in range(size):
        diagonal.append((row_col, row_col))
    yield diagonal

    diagonal = []
    for row_col in range(size):
        diagonal.append((row_col, size - 1 - row_col))
    yield diagonal


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
