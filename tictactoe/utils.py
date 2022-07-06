from functools import cache


@cache
def get_line_sets(size):
    all_sets = []

    for row in range(size):
        row_set = set()
        for col in range(size):
            row_set.add((row, col))
        all_sets.append(row_set)

    for col in range(size):
        col_set = set()
        for row in range(size):
            col_set.add((row, col))
        all_sets.append(col_set)

    diag_set = set()
    for row_col in range(size):
        diag_set.add((row_col, row_col))
    all_sets.append(diag_set)

    diag_set = set()
    for row_col in range(size):
        diag_set.add((row_col, size - 1 - row_col))
    all_sets.append(diag_set)

    return all_sets


def init_grid(size, value):
    return [[value for _ in range(size)] for _ in range(size)]


def print_grid(grid):
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
