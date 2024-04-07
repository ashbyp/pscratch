question = "https://adventofcode.com/2016/day/14"
input_data = "https://adventofcode.com/2016/day/14/input"

pdata = """qzyelonm"""

tdata = """abc"""


def part1(data: str, debug: bool = False):
    pass


def has_triple(h: str):
    for i in range(0, len(h) - 2, 1):
        if h[i] == h[i + 1] == h[i + 2]:
            return h[i]
    return None


def all_fives(h: str):
    s = set()
    for i in range(0, len(h) - 4, 1):
        if h[i] == h[i + 1] == h[i + 2] == h[i + 3] == h[i + 4]:
            s.add(h[i])
    return s

CACHE = {}

def hhhh(s):
    if s in CACHE:
        return CACHE[s]
    import hashlib
    h = s.encode("utf-8")
    h = hashlib.md5(h).hexdigest()
    # print(h)
    for _ in range(2016):
        h = h.encode("utf-8")
        h = hashlib.md5(h).hexdigest()
        # print(h)
    CACHE[s] = h
    return h

def check(triple, salt, cache, idx):
    # print('check', triple, 'at', idx-1)
    import hashlib
    # print('check', triple, 'at', idx)
    for tries in range(1000):
        fives = cache.get(idx + tries)
        if fives is None:
            s = salt + str(idx + tries)
            v = hhhh(s)
            fives = all_fives(v)
            cache[idx] = fives
        if triple in fives:
            print('  found at ', idx+tries)
            return True
    return False


def part2(data: str, debug: bool = False):
    import hashlib
    found = 0
    cache = {}
    i = 0
    while found < 64:
        s = data + str(i)
        v = hhhh(s)
        t = has_triple(v)
        if t:
            if check(t, data, cache, i + 1):
                found += 1
                print('found', found)
        i += 1
    print(i-1)


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
    run("Part 2 puzzle", pdata, part2, False)

if __name__ == '__main__':
    main()
    # print(hhhh('abc0'))