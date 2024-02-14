pdata = """157,222,1,2,177,254,0,228,159,140,249,187,255,51,76,30"""

tdata = """3, 4, 1, 5"""


def sub(data, start, size):
    bef = data[start:start + size]
    aft = data[0:size - (len(bef))]
    return bef + aft


def replace(data, new_data, start):
    for i, d in enumerate(new_data):
        data[(start + i) % len(data)] = d


def part2(data: str, debug: bool = False):
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

    s = ''.join([f'{d:02x}' for d in dense])
    print(s)


def part1(data: str, debug: bool = False):
    if data == tdata:
        clist = list(range(5))
    else:
        clist = list(range(256))

    pos, skip = 0, 0
    data = list(map(int, data.split(',')))

    if debug:
        print(clist, data)

    for l in data:
        if l > len(clist):
            continue
        to_rev = sub(clist, pos, l)
        replace(clist, reversed(to_rev), pos)
        pos = (pos + l + skip) % len(clist)
        skip += 1

    if debug:
        print(clist)

    print(clist[0] * clist[1])


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
