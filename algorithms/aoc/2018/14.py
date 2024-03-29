question = "https://adventofcode.com/2018/day/14"
input_data = "https://adventofcode.com/2018/day/14/input"

pdata = "505961"

tdata = "59414"


def part2(data: str, debug: bool = False):
    recipes = [3, 7]
    check = [int(i) for i in data]
    e1 = 0
    e2 = 1

    while True:

        e1_s, e2_s = recipes[e1], recipes[e2]
        s = e1_s + e2_s
        for c in str(s):
            recipes.append(int(c))

            if len(recipes) >= len(check):
                if recipes[-len(check):] == check:
                    print(len(recipes) - len(check))
                    return

        e1 += (1 + e1_s)
        e2 += (1 + e2_s)
        e1 %= len(recipes)
        e2 %= len(recipes)


def part1(data: str, debug: bool = False):
    recipes = [3, 7]
    times = int(data)
    e1 = 0
    e2 = 1

    while len(recipes) < times + 10 + 1:
        e1_s, e2_s = recipes[e1], recipes[e2]
        s = e1_s + e2_s
        for c in str(s):
            recipes.append(int(c))
        e1 += (1 + e1_s)
        e2 += (1 + e2_s)
        e1 %= len(recipes)
        e2 %= len(recipes)

    print(''.join(map(str, recipes[times:times + 10])))


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
