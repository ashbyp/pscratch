question = "https://adventofcode.com/2020/day/11"
input_data = "https://adventofcode.com/2020/day/11/input"

pdata = """LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLL..LLLLLLLL.LLLLLLLL.LLLLLLLL..LLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL..LLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLL.LLL.LLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.L.LLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
LLLLL.LLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLLL.LLL.LLLL.LLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LL.LLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLL.LLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL...LLLLLLLLLLL.
LL..LL..L..L.L...L.L..L.L....L.LL..L.L......LL.LL....LL..LL..LLLL.L.LLL.L.....LLL.LL........L.....
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLL..LL.LLLLLLL.LL.LLL.LLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLL.LL.LLLLLLL..LLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL..LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.L.LLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
...........L.....L............LL..L...LL...L.LLL.L....L.L.L......L..L...LL......L.L.L.........LL..
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LL.LLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL..LLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
............L......L......L...L....L.....LLL....L.......L.....L.L..L....L..L.L....LL.....L....L.L.
LLLLLLLLLL..LLLLLLLLLLLLLL.LLLL.LLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL
LLLL.LLLLL.LLLLLL.LLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
.LL........L.......L....LL.L..L.L...L.LLLLLL.L..............L.L.........LL........L....L.LL.....L.
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLL.L.LLLLLLL.LLLLL.LLLLLLLL.LLLLL.LL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LL.LLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLL.
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
...L..L..L.LL.L.L.L......L.LLLL.L..L.L..L..L.L...L.LL.L...L....LL..L.L..L.L...........L.L..L..LL..
LLLLLL.LLL.LLLLLLLLL.LLLLLLLLL.L.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLL.LLLL.LLL.LLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.L.LLLLLLLLLLLLLLL..LLLLLLL.LLLLLLLLL.LLLLLLLLLLLL.L
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLL.LL.LLLLLLLLLLLL.LLLLL.L.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLL.LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.L.LLL..LLL.LLL.LLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
...LL.L..L..........L......L.L..L.LL.......LL...L.LL..L.L..L.L......L..L......L..L..L..L.L........
LLLLLLL.LL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLL.LLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.L.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLL.LLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLL.LLL.LLL.L.LLLLLLLLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL
LLLLLLL.LLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLLLLLL.L.LLLLLLLL.LLLLLLL.LLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
L.....L..LL.L.......L.L..L....L..L.L...L.LLLL.......L.L...L....LL.L...L.L.L.LL.L......L.L.L.L.L...
LLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL..L.LLLLLLLLLLLLLLLLLLLLL
L.LLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL..LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLL.LLLLLLL..LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
.......L..L..L.L....LLLLLL..L..LL.LLL..LL..L..L...L...LL.....L..LL.LL..L.L..L.L..L.L.L....LL....L.
LLLLLLLLLLLLLLLL.LLL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLL.LLLL.LLLLLLLLL.L.LLLLLLLLLLLL
LLLLLLL.LL.LLLLLLLLLLLL.LL.LLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLLL.LL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLL.LL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLLLLLLLL.LLLLLLLL.LLLLL
.....L.L..L.......L.LL..........L...LLLL.LL..L...L.L.L.LLLL...L.....L...L.LLLLLL..L..........LL...
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL..LLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLL.L.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLL
L.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLL
..L.........L..L.L...L................LLL..L..LLL.L......L....L.L.....L.L.L.L.L..L.L.L.L....L....L
LLLLLLLLLL..LLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LL.LLLLLL.LLLLLLLLLLLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLL.
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLL.L.LLLLLL.LLLLL
LLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLL.LLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLL..LLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL
...LLL.....L..L.LL.L.L.LL.....L..LL.LLLL...L.L....LL.L...L..LL...L..LLL......LL..L..L.L..L.L...LL.
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLL.LLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLLLLL.LLLLLLLLL.LLLL.LLLLLLLL.LLLLLLLL.LL.LLLLL.LLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLL.LLLLLLLL.LLLLLLLLLL.LLLLLLLLLLLLLLL.LL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLL.LLLLLLLLL.LLLLLL.L.LLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLL..LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.L.LLLLLL.LLLLL
LL.LLLLLL..LLLLLLLLL.LLLLL.LLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLL.LLLLL.LLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LLLLL.LLLLLLLL..LLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLL
...L....L..L.L..L..L.LLLL....L..L.....L.....L.L..L.L.L...L.L.........L....L..L..L.LL.L...L.L...L..
LLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL..LLLLL.LL.LLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LLLL..LLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL..LL.LLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LL.LL
LLLLLLLLLL.LLLLLLLLL.LLLLL.LLLLL.L.LLLLL.LLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
LLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLL.LLLLLLL.LLLLL
LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLLLL..LLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL..LLLLLLLL.LLLLLLLL.LLLLL
LLLLLL.L.L.LLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLL.LLLLLLLL.LLLLL
L.LLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLL.LLL..LLLL"""

tdata = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

adj = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def see_any(grid: list[list[str]], row: int, col: int, nrows: int, ncols: int) -> bool:
    for dr, dc in adj:
        step = 1
        while True:
            nr, nc = row + (dr * step), col + (dc * step)
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc] == '#':
                    return True
                elif grid[nr][nc] == 'L':
                    break
                else:
                    step += 1
            else:
                break

    return False


def how_many(grid: list[list[str]], row: int, col: int, nrows: int, ncols: int) -> int:
    occupied = 0

    for dr, dc in adj:
        # print(dr, dc)
        step = 1
        while True:
            nr, nc = row + (dr * step), col + (dc * step)
            # print("  ", nr, nc)
            if 0 <= nr < nrows and 0 <= nc < ncols:
                if grid[nr][nc] == '#':
                    occupied += 1
                    break
                elif grid[nr][nc] == 'L':
                    break
                step += 1
            else:
                break

    return occupied


def part2(data: str, debug: bool = False):
    grid = list(list(row) for row in data.splitlines())
    nrows, ncols = len(grid), len(grid[0])

    print(nrows, ncols)

    if debug:
        print(grid)

    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, 
    the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also 
    occupied, the seat becomes empty.
    Otherwise, the seat's state does not change."""

    try:
        while True:
            new_grid = [[' ' for _ in range(ncols)] for _ in range(nrows)]
            moved = False

            for row in range(nrows):
                for col in range(ncols):
                    if grid[row][col] == '.':
                        new_grid[row][col] = '.'
                    elif grid[row][col] == 'L':
                        if not see_any(grid, row, col, nrows, ncols):
                            new_grid[row][col] = '#'
                            moved = True
                        else:
                            new_grid[row][col] = 'L'

                    elif grid[row][col] == '#':
                        if how_many(grid, row, col, nrows, ncols) >= 5:
                            moved = True
                            new_grid[row][col] = 'L'
                        else:
                            new_grid[row][col] = '#'

                    else:
                        raise ValueError()

            grid = new_grid

            if debug:
                print(grid)
                print(sum(1 if grid[row][col] == '#' else 0 for row in range(nrows) for col in range(ncols)))

            if not moved:
                break
    except Exception as e:
        print(e)

    print(sum(1 if grid[row][col] == '#' else 0 for row in range(nrows) for col in range(ncols)))


def part1(data: str, debug: bool = False):
    grid = list(list(row) for row in data.splitlines())
    nrows, ncols = len(grid), len(grid[0])

    print(nrows, ncols)

    if debug:
        print(grid)

    try:
        while True:
            new_grid = [[' ' for _ in range(ncols)] for _ in range(nrows)]
            moved = False

            for row in range(nrows):
                for col in range(ncols):
                    if grid[row][col] == '.':
                        new_grid[row][col] = '.'
                    elif grid[row][col] == 'L':
                        free = True
                        for dr, dc in adj:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < nrows and 0 <= nc < ncols:
                                if grid[nr][nc] == '#':
                                    free = False
                                    break
                        if free:
                            new_grid[row][col] = '#'
                            moved = True
                        else:
                            new_grid[row][col] = 'L'

                    elif grid[row][col] == '#':
                        occupied = 0
                        for dr, dc in adj:
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < nrows and 0 <= nc < ncols:
                                if grid[nr][nc] == '#':
                                    occupied += 1
                        if occupied >= 4:
                            moved = True
                            new_grid[row][col] = 'L'
                        else:
                            new_grid[row][col] = '#'

                    else:
                        raise ValueError()

            grid = new_grid

            if debug:
                print(grid)
                print(sum(1 if grid[row][col] == '#' else 0 for row in range(nrows) for col in range(ncols)))

            if not moved:
                break
    except Exception as e:
        print(e)

    print(sum(1 if grid[row][col] == '#' else 0 for row in range(nrows) for col in range(ncols)))


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    run("Part 1 test", tdata, part1, True)
    # run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
