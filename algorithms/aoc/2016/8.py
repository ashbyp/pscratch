pdata = """rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=0 by 10
rotate column x=5 by 2
rotate column x=0 by 1
rect 9x1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 5
rotate row y=0 by 5
rotate column x=0 by 1
rect 4x1
rotate column x=40 by 1
rotate column x=27 by 1
rotate column x=22 by 1
rotate column x=17 by 1
rotate column x=12 by 1
rotate column x=7 by 1
rotate column x=2 by 1
rotate row y=2 by 5
rotate row y=1 by 3
rotate row y=0 by 5
rect 1x3
rotate row y=2 by 10
rotate row y=1 by 7
rotate row y=0 by 2
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 5
rotate row y=1 by 3
rotate row y=0 by 3
rect 1x3
rotate column x=45 by 1
rotate row y=2 by 7
rotate row y=1 by 10
rotate row y=0 by 2
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 4x1
rotate row y=2 by 13
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 8
rotate row y=0 by 5
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate row y=3 by 17
rotate row y=2 by 20
rotate row y=0 by 15
rotate column x=13 by 1
rotate column x=12 by 3
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=0 by 1
rect 14x1
rotate row y=1 by 47
rotate column x=9 by 1
rotate column x=4 by 1
rotate row y=3 by 3
rotate row y=2 by 10
rotate row y=1 by 8
rotate row y=0 by 5
rotate column x=2 by 2
rotate column x=0 by 2
rect 3x2
rotate row y=3 by 12
rotate row y=2 by 10
rotate row y=0 by 10
rotate column x=8 by 1
rotate column x=7 by 3
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate row y=0 by 20
rotate column x=46 by 1
rotate row y=4 by 17
rotate row y=3 by 10
rotate row y=2 by 10
rotate row y=1 by 5
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 2
rotate column x=1 by 1
rotate column x=0 by 1
rect 9x1
rotate column x=32 by 4
rotate row y=4 by 33
rotate row y=3 by 5
rotate row y=2 by 15
rotate row y=0 by 15
rotate column x=13 by 1
rotate column x=12 by 3
rotate column x=10 by 1
rotate column x=8 by 1
rotate column x=7 by 2
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 14x1
rotate column x=39 by 3
rotate column x=35 by 4
rotate column x=20 by 4
rotate column x=19 by 3
rotate column x=10 by 4
rotate column x=9 by 3
rotate column x=8 by 3
rotate column x=5 by 4
rotate column x=4 by 3
rotate row y=5 by 5
rotate row y=4 by 5
rotate row y=3 by 33
rotate row y=1 by 30
rotate column x=48 by 1
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 1
rotate column x=43 by 1
rotate column x=38 by 3
rotate column x=37 by 3
rotate column x=36 by 5
rotate column x=35 by 1
rotate column x=33 by 1
rotate column x=32 by 5
rotate column x=31 by 5
rotate column x=30 by 1
rotate column x=23 by 4
rotate column x=22 by 3
rotate column x=21 by 3
rotate column x=20 by 1
rotate column x=12 by 2
rotate column x=11 by 2
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 3
rotate column x=0 by 4"""

tdata = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""


def p_grid(g):
    n_rows, n_cols = len(g), len(g[0])
    for row in range(n_rows):
        for col in range(n_cols):
            print(g[row][col], end='')
        print()


def part2(data: str, debug: bool = False):
    if data == tdata:
        n_rows = 3
        n_cols = 7
    else:
        n_rows = 6
        n_cols = 50

    grid = [['.' for _ in range(n_cols)] for _ in range(n_rows)]
    if debug:
        p_grid(grid)

    for line in data.splitlines():
        ins = line.split(' ')
        if ins[0] == 'rect':
            width, height = ins[1].split('x')
            for row in range(int(height)):
                for col in range(int(width)):
                    grid[row][col] = '#'
        elif ins[1] == 'column':
            col = int(ins[2].split('=')[1])
            shift = int(ins[4])

            new_col = ['.' for _ in range(n_rows)]
            for row in range(n_rows):
                new_col[(row + shift) % n_rows] = grid[row][col]

            for row, val in enumerate(new_col):
                grid[row][col] = val

        elif ins[1] == 'row':
            row = int(ins[2].split('=')[1])
            shift = int(ins[4])

            new_row = ['.' for _ in range(n_cols)]
            for col in range(n_cols):
                new_row[(col + shift) % n_cols] = grid[row][col]

            for col, val in enumerate(new_row):
                grid[row][col] = val

        else:
            raise ValueError(line)

    print()
    p_grid(grid)


def part1(data: str, debug: bool = False):
    if data == tdata:
        n_rows = 3
        n_cols = 7
    else:
        n_rows = 6
        n_cols = 50

    grid = [['.' for _ in range(n_cols)] for _ in range(n_rows)]
    if debug:
        p_grid(grid)

    for line in data.splitlines():
        ins = line.split(' ')
        if ins[0] == 'rect':
            width, height = ins[1].split('x')
            for row in range(int(height)):
                for col in range(int(width)):
                    grid[row][col] = '#'
        elif ins[1] == 'column':
            col = int(ins[2].split('=')[1])
            shift = int(ins[4])

            new_col = ['.' for _ in range(n_rows)]
            for row in range(n_rows):
                new_col[(row + shift) % n_rows] = grid[row][col]

            for row, val in enumerate(new_col):
                grid[row][col] = val

        elif ins[1] == 'row':
            row = int(ins[2].split('=')[1])
            shift = int(ins[4])

            new_row = ['.' for _ in range(n_cols)]
            for col in range(n_cols):
                new_row[(col + shift) % n_cols] = grid[row][col]

            for col, val in enumerate(new_row):
                grid[row][col] = val

        else:
            raise ValueError(line)

        if debug:
            print()
            p_grid(grid)

    from collections import Counter
    print(Counter([grid[r][c] for r in range(n_rows) for c in range(n_cols)]))


if __name__ == '__main__':
    def run(msg, data, fn, debug):
        if data:
            print(f'{msg:15} ------------')
            fn(data, debug)
            print()


    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)
