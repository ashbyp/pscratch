question = "https://adventofcode.com/2016/day/13"
input_data = "https://adventofcode.com/2016/day/13/input"

pdata = """1352,31,39"""

tdata = """10,7,4"""


def is_wall(x, y, key):
    z = x * x + 3 * x + 2 * x * y + y + y * y + key
    b = f'{z:b}'
    return sum(1 for c in b if c == '1') % 2 == 1


def visited1(start: tuple[int, int], key: int) -> int:
    from collections import deque
    queue = deque()
    visited = set()
    queue.append((start, 0))
    visited.add(start)
    while queue:
        c = queue.popleft()
        visited.add(c[0])
        print(' ', c)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            n = (c[0][0] + dx, c[0][1] + dy)
            print('   ', n, is_wall(n[0], n[1], key))
            if n[0] >= 0 and n[1] >= 0 and not is_wall(n[0], n[1], key) and n not in visited:
                if c[1] + 1 <= 50:
                    queue.append((n, c[1] + 1))
    return len(visited)


def part2(data: str, debug: bool = False):
    key, tx, ty = map(int, data.split(','))
    start = (1, 1)

    grid = [['#' if is_wall(x, y, key) else ' ' for x in range(10)] for y in range(7)]
    if debug:
        for row in grid:
            print(row)

    print(f'Visited: {visited1(start, key)}')


def shortest(start: tuple[int, int], end: tuple[int, int], key: int) -> int:
    from collections import deque
    queue = deque()
    visited = set()
    queue.append((start, 0))
    while queue:
        c = queue.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            n = (c[0][0] + dx, c[0][1] + dy)
            if n == end:
                return c[1] + 1
            if n[0] >= 0 and n[1] >= 0 and not is_wall(n[0], n[1], key) and n not in visited:
                queue.append((n, c[1] + 1))
                visited.add(c[0])


def part1(data: str, debug: bool = False):
    key, tx, ty = map(int, data.split(','))
    start = (1, 1)
    end = (tx, ty)

    grid = [['#' if is_wall(x, y, key) else ' ' for x in range(10)] for y in range(7)]
    if debug:
        for row in grid:
            print(row)

    if debug:
        print(f'Find {start} -> {end}, key={key}')

    print(f'Shortest: {shortest(start, end, key)}')


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    # run("Part 1 test", tdata, part1, True)
    # run("Part 1 puzzle", pdata, part1, False)
    # run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, True)


if __name__ == '__main__':
    main()
