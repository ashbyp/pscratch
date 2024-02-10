pdata = """Dummy not used"""

tdata = """Dummy also not used"""


def play(p_h, p_d, p_a, b_h, b_d, b_a, debug=False):
    player = True
    while True:
        if player:
            b_h -= max(p_d - b_a, 1)
            if b_h <= 0:
                return player
        else:
            p_h -= max(b_d - p_a, 1)
            if p_h <= 0:
                return player
        player = not player

        if debug:
            print('player', p_h, 'boss', b_h)


def poss():
    from itertools import combinations

    p = []

    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    amour = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
    rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

    for w in weapons:
        p.append(w)

    for w in weapons:
        for a in amour:
            p.append((w[0] + a[0], w[1] + a[1], w[2] + a[2]))

    for w in weapons:
        for a in amour:
            for r in rings:
                p.append((w[0] + a[0] + r[0], w[1] + a[1] + r[1], w[2] + a[2] + r[2]))

    for w in weapons:
        for rc in combinations(rings, 2):
            p.append((
                w[0] + sum(r[0] for r in rc),
                w[1] + sum(r[1] for r in rc),
                w[2] + sum(r[2] for r in rc),
            ))

    for w in weapons:
        for a in amour:
            for rc in combinations(rings, 2):
                p.append((
                    w[0] + a[0] + sum(r[0] for r in rc),
                    w[1] + a[1] + sum(r[1] for r in rc),
                    w[2] + a[2] + sum(r[2] for r in rc),
                ))
    return p


def part2(data: str, debug: bool = False):
    if data != pdata:
        return
    max_cost = 0
    for cost, damage, amour in poss():
        if not play(100, damage, amour, 109, 8, 2):
            max_cost = max(cost, max_cost)
    print(max_cost)


def part1(data: str, debug: bool = False):
    if data == tdata:
        p_h, p_d, p_a = 8, 5, 5
        b_h, b_d, b_a = 12, 7, 2

        winner = play(p_h, p_d, p_a, b_h, b_d, b_a, debug)
        if debug:
            print(winner)
    else:
        min_cost = float('inf')
        for cost, damage, amour in poss():
            if play(100, damage, amour, 109, 8, 2):
                min_cost = min(cost, min_cost)

        print(min_cost)


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
