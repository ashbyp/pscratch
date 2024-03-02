question = "https://adventofcode.com/2020/day/13"
input_data = "https://adventofcode.com/2020/day/13/input"

pdata = """1000299
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,971,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,23,x,x,x,x,x,29,x,487,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"""

tdata = """939
7,13,x,x,59,x,31,19"""

tdata = """100
17,x,13,19"""

tdata="""100
67,7,59,61"""

tdata="""100
67,x,7,59,61"""

tdata="""100
67,7,x,59,61"""

tdata="""100
1789,37,47,1889"""


def part2(data: str, debug: bool = False):
    debug=False

    import numpy as np

    data = data.splitlines()
    _ = int(data[0])
    deps = list(enumerate([int(d) for d in data[1].split(',') if d != 'x']))
    min_start = int(deps[0][1])
    if debug:
        print(deps)

    ts = 0
    valid = []
    while True:
        if ts > 100000000000000 and ts % 1_000_000 == 0:
            print(ts)

        valid = []
        for dd in deps:
            d = dd[1]
            div = ts // d
            times = d * div + (d if (d * div) < ts else 0)
            diff = times - ts
            if debug:
                print('ts=', ts, 'dep=', d, 'diff=', diff)
            if diff != dd[0]:
                break
            else:
                valid.append(dd[0])
        else:
            print(ts)
            return
        if debug:
            print()

        if len(valid) > num_valid and ts != 0:
            num_valid = len(valid)
            min_start = ts
            print('min start is now', min_start)
        ts += min_start

    print('not found')


def part1(data: str, debug: bool = False):
    data = data.splitlines()
    ts = int(data[0])
    deps = list(map(int, filter(lambda x: x != 'x', data[1].split(','))))
    if debug:
        print(ts, deps)

    ans = 0
    min_wait = float('inf')

    for d in deps:
        div = ts // d
        rem = ts % d
        times = d * div + d
        diff = times - ts
        if debug:
            print(d, 'div', div, 'rem', rem, 'times', times, 'diff', diff)
        if diff < min_wait:
            min_wait = diff
            ans = d * diff

    print(ans)


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
    run("Part 2 test", tdata, part2, True)
    # run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
