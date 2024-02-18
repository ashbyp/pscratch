question = "https://adventofcode.com/2018/day/11"
input_data = "https://adventofcode.com/2018/day/11/input"

pdata = """7857"""

tdata = """"""


def check(grid, size, square_size):
    best = float('-inf')
    coord = None
    for x in range(size - square_size - 1):
        for y in range(size - square_size - 1):
            cur = 0
            for i in range(x, x + square_size):
                for j in range(y, y + square_size):
                    cur += grid[i][j]
            if cur > best:
                best = cur
                coord = (x, y)
    return best, coord


def part2(data: str, debug: bool = False):
    serial = int(data)
    size = 300

    grid = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            rack_id = x + 1 + 10
            power = rack_id * (y + 1)
            power += serial
            power *= rack_id
            power = power // 100 % 10
            power -= 5
            grid[x][y] = power

    best = float('-inf')
    coord = None
    best_size = None
    for sqsize in range(1, 300):
        print('Check', sqsize)
        b, c = check(grid, size, sqsize)
        if b > best:
            best = b
            coord = c
            best_size = sqsize

    print(best, coord, best_size, 'add 1 to x and y')


def part1(data: str, debug: bool = False):
    serial = int(data)
    size = 300

    grid = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            rack_id = x + 1 + 10
            power = rack_id * (y + 1)
            power += serial
            power *= rack_id
            power = power // 100 % 10
            power -= 5
            grid[x][y] = power

    best = float('-inf')
    coord = None
    for x in range(size - 2):
        for y in range(size - 2):
            cur = 0
            if debug:
                print('scan', x, y)
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if debug:
                        print(' ', i, j)
                    cur += grid[i][j]
            if cur > best:
                best = cur
                coord = (x, y)

    print(best, coord)


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')
            print()

    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
