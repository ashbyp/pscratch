pdata = """34000000"""

tdata = """150"""

import math

def divisors(n):
    d = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            d.append(i)
    d.append(n)
    return d


def divisors1(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, int(n / i)])
    divs.extend([n])
    return list(set(divs))


def part2(data: str, debug: bool = False):
    target = int(data)
    for i in range(1, 10000000000000000):
        d = divisors1(i)
        di = sum(x for x in d if i // x <= 50)
        p = di * 11
        if p >= target:
            print(i)
            break
        if debug:
            if i % 10000 == 0:
                print(i, 'p=', p, 'diff=', target - p)


def part1(data: str, debug: bool = False):
    target = int(data)
    for i in range(1, 10000000000000000):
        d = divisors1(i)
        if debug:
            print('Num:', i, 'Divisors:', d)
        p = sum(d) * 10
        if p >= target:
            print(i)
            break
        if debug:
            if i % 10000 == 0:
                print(i, 'p=', p, 'diff=', target - p)


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

    # run("Part 1 test", tdata, part1, True)
    # run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, True)


if __name__ == '__main__':
    main()
