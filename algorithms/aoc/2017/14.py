pdata = """hfdlxzhv"""

tdata = """flqrgnkx"""


def knot(data):
    def sub(_data, _start, _size):
        bef = _data[_start:_start + _size]
        aft = _data[0:_size - (len(bef))]
        return bef + aft

    def replace(_data, _new_data, _start):
        for i, d in enumerate(_new_data):
            _data[(_start + i) % len(_data)] = d

    clist = list(range(256))
    pos, skip = 0, 0
    data = [ord(x) for x in data] + [17, 31, 73, 47, 23]

    for _ in range(64):
        for l in data:
            if l > len(clist):
                continue
            to_rev = sub(clist, pos, l)
            replace(clist, reversed(to_rev), pos)
            pos = (pos + l + skip) % len(clist)
            skip += 1

    dense = []

    for i in range(0, 256, 16):
        z = clist[i]
        for j in range(i + 1, i + 16):
            z = z ^ clist[j]
        dense.append(z)

    hex_no = ''.join([f'{d:02x}' for d in dense])
    b = ''
    for h in hex_no:
        b += f'{int(h, 16):04b}'

    return b


def part2(data: str, debug: bool = False):
    grid = []

    for i in range(128):
        r = knot(data + "-" + str(i))
        grid.append([1 if x == '1' else 0 for x in r])

    visited = set()

    def search(x, y, l):
        if not (0 <= x < 128 and 0 <= y < 128) or (x, y) in visited:
            return
        visited.add((x, y))

        if grid[x][y] == 0:
            return

        grid[x][y] = l
        search(x + 1, y, l)
        search(x - 1, y, l)
        search(x, y + 1, l)
        search(x, y - 1, l)

    label = 1
    for row in range(128):
        for col in range(128):
            if grid[row][col] == 1 and not (row, col) in visited:
                search(row, col, label)
                label += 1

    if debug:
        for r in grid: print(r)

    print(label - 1)


def part1(data: str, debug: bool = False):
    tot = 0
    for i in range(128):
        r = knot(data + "-" + str(i))
        tot += sum(1 if x == '1' else 0 for x in r)
    print(tot)


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
