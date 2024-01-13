pdata = """4,3,4,5,2,1,1,5,5,3,3,1,5,1,4,2,2,3,1,5,1,4,1,2,3,4,1,4,1,5,2,1,1,3,3,5,1,1,1,1,4,5,1,2,1,2,1,1,1,5,3,3,1,1,1,1,2,4,2,1,2,3,2,5,3,5,3,1,5,4,5,4,4,4,1,1,2,1,3,1,1,4,2,1,2,1,2,5,4,2,4,2,2,4,2,2,5,1,2,1,2,1,4,4,4,3,2,1,2,4,3,5,1,1,3,4,2,3,3,5,3,1,4,1,1,1,1,2,3,2,1,1,5,5,1,5,2,1,4,4,4,3,2,2,1,2,1,5,1,4,4,1,1,4,1,4,2,4,3,1,4,1,4,2,1,5,1,1,1,3,2,4,1,1,4,1,4,3,1,5,3,3,3,4,1,1,3,1,3,4,1,4,5,1,4,1,2,2,1,3,3,5,3,2,5,1,1,5,1,5,1,4,4,3,1,5,5,2,2,4,1,1,2,1,2,1,4,3,5,5,2,3,4,1,4,2,4,4,1,4,1,1,4,2,4,1,2,1,1,1,1,1,1,3,1,3,3,1,1,1,1,3,2,3,5,4,2,4,3,1,5,3,1,1,1,2,1,4,4,5,1,5,1,1,1,2,2,4,1,4,5,2,4,5,2,2,2,5,4,4"""

tdata = """3,4,3,1,2"""


def part2(data: str, debug: bool = False):
    data = list(map(int, data.split(',')))
    fish = {}
    for d in data:
        if d in fish:
            fish[d] = fish[d] + 1
        else:
            fish[d] = 1

    print(fish)

    for i in range(256):
        fishes = fish.copy()
        fish = {}
        if 0 in fishes:
            fish[6] = fishes[0]
            fish[8] = fishes[0]

        for i in range(1, 9):
            if i in fishes:
                fish[i - 1] = fish.get(i - 1, 0) + fishes[i]

    print(sum(v for v in fish.values()))


def part1(data: str, debug: bool = False):
    fish = list(map(int, data.split(',')))
    for i in range(80):
        fishes = fish.copy()
        fish = []
        for f in fishes:
            if f == 0:
                fish.append(6)
                fish.append(8)
            else:
                fish.append(f - 1)
    print(len(fish))


if __name__ == '__main__':
    def run(msg, data, fn, debug):
        if data:
            print(f'{msg:15} ------------')
            fn(data, debug)
            print()


    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)
