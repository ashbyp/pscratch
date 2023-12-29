def part2():
    target = 347991
    # target = 200
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    pop = {(0, 0): 1}

    def get_n(_x, _y):
        cells = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
        n = 0
        for c in cells:
            cx = _x + c[0]
            cy = _y + c[1]
            n += pop.get((cx, cy), 0)
        return n

    i = 1
    n = 1
    moves = 1
    x, y = 0, 0
    while True:
        # print(' at ', x, y)
        # print('moves', moves)
        d = dirs[(i - 1) % 4]

        for _ in range(moves):
            x = x + d[0]
            y = y + d[1]
            n = get_n(x, y)
            if n > target:
                break
            pop[(x, y)] = n

            # print(x, y, n)

        if n > target:
            break

        if i % 2 == 0:
            moves += 1
        i += 1

    print(n)


def part1():
    target = 347991
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    i = 1
    n = 1
    moves = 1
    x, y = 0, 0
    while True:
        # print(' at ', x, y)
        # print('moves', moves)
        d = dirs[(i - 1) % 4]

        for _ in range(moves):
            x = x + d[0]
            y = y + d[1]
            n += 1
            if n == target:
                break

        if n == target:
            break

        if i % 2 == 0:
            moves += 1
        i += 1

    print(abs(x) + abs(y))


if __name__ == '__main__':
    part1()
    part2()
