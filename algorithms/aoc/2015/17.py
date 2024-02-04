pdata = """43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38"""

tdata = """20
15
10
5
5
"""


def part2(data: str, debug: bool = False):
    from itertools import combinations
    target = 25 if data == tdata else 150
    sizes = [int(i) for i in data.splitlines()]
    counts = []

    for l in range(1, len(sizes)):
        for perm in combinations(sizes, l):
            if sum(perm) == target:
                counts.append(l)
    print(sorted(counts).count(sorted(counts)[0]))


def part1(data: str, debug: bool = False):
    from itertools import combinations
    target = 25 if data == tdata else 150
    sizes = [int(i) for i in data.splitlines()]
    tot = 0

    for l in range(1, len(sizes)):
        for perm in combinations(sizes, l):
            if sum(perm) == target:
                tot += 1
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
