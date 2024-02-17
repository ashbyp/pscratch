question = "https://adventofcode.com/2016/day/15"
input_data = "https://adventofcode.com/2016/day/15/input"

pdata = """Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0."""

tdata = """Disc #1 has 17 positions; at time=0, it is at position 5.
Disc #2 has 19 positions; at time=0, it is at position 8.
Disc #3 has 7 positions; at time=0, it is at position 1.
Disc #4 has 13 positions; at time=0, it is at position 7.
Disc #5 has 5 positions; at time=0, it is at position 1.
Disc #6 has 3 positions; at time=0, it is at position 0."""


def part2(data: str, debug: bool = False):
    discs = [
        (17, 5),
        (19, 8),
        (7, 1),
        (13, 7),
        (5, 1),
        (3, 0),
        (11, 0),
    ]

    for second in range(1, 100000000):
        for i, disc in enumerate(discs, start=1):
            pos = (disc[1] + second + i) % disc[0]
            if pos != 0:
                break
        else:
            print(second)
            return


def part1(data: str, debug: bool = False):
    discs = [
        (17, 5),
        (19, 8),
        (7, 1),
        (13, 7),
        (5, 1),
        (3, 0),
    ]

    for second in range(1, 100000000):
        for i, disc in enumerate(discs, start=1):
            pos = (disc[1] + second + i) % disc[0]
            if pos != 0:
                break
        else:
            print(second)
            return


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
