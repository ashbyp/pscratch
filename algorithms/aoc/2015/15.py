pdata = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

tdata = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""


def part2(data: str, debug: bool = False):
    ingredients = []
    for line in data.splitlines():
        words = line.replace(',', '').split()
        ingredients.append((words[0], int(words[2]), int(words[4]),
                            int(words[6]), int(words[8]), int(words[10])))

    if debug:
        print(ingredients)

    if data == pdata:
        best = 0
        for i in range(1, 101):
            for j in range(1, 101):
                for k in range(1, 101):
                    for l in range(1, 101):
                        if (i + j + k + l) == 100:
                            c = max(i * ingredients[0][1] + j * ingredients[1][1] + k * ingredients[2][1] + l *
                                    ingredients[3][1], 0)
                            d = max(i * ingredients[0][2] + j * ingredients[1][2] + k * ingredients[2][2] + l *
                                    ingredients[3][2], 0)
                            f = max(i * ingredients[0][3] + j * ingredients[1][3] + k * ingredients[2][3] + l *
                                    ingredients[3][3], 0)
                            t = max(i * ingredients[0][4] + j * ingredients[1][4] + k * ingredients[2][4] + l *
                                    ingredients[3][4], 0)

                            cal = max(i * ingredients[0][5] + j * ingredients[1][5] + k * ingredients[2][5] + l *
                                      ingredients[3][5], 0)

                            if cal == 500:
                                s = c * d * f * t
                                best = max(best, s)
        print(best)


def part1(data: str, debug: bool = False):
    ingredients = []
    for line in data.splitlines():
        words = line.replace(',', '').split()
        ingredients.append((words[0], int(words[2]), int(words[4]),
                            int(words[6]), int(words[8]), int(words[10])))

    if debug:
        print(ingredients)

    if data == tdata:
        best = 0
        for i in range(1, 101):
            for j in range(1, 101):
                if (i + j) == 100:
                    c = max(i * ingredients[0][1] + j * ingredients[1][1], 0)
                    d = max(i * ingredients[0][2] + j * ingredients[1][2], 0)
                    f = max(i * ingredients[0][3] + j * ingredients[1][3], 0)
                    t = max(i * ingredients[0][4] + j * ingredients[1][4], 0)
                    s = c * d * f * t
            best = max(best, s)
        print(best)
    else:
        best = 0
        for i in range(1, 101):
            for j in range(1, 101):
                for k in range(1, 101):
                    for l in range(1, 101):
                        if (i + j + k + l) == 100:
                            c = max(i * ingredients[0][1] + j * ingredients[1][1] + k * ingredients[2][1] + l *
                                    ingredients[3][1], 0)
                            d = max(i * ingredients[0][2] + j * ingredients[1][2] + k * ingredients[2][2] + l *
                                    ingredients[3][2], 0)
                            f = max(i * ingredients[0][3] + j * ingredients[1][3] + k * ingredients[2][3] + l *
                                    ingredients[3][3], 0)
                            t = max(i * ingredients[0][4] + j * ingredients[1][4] + k * ingredients[2][4] + l *
                                    ingredients[3][4], 0)

                            s = c * d * f * t
                            best = max(best, s)
        print(best)


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
