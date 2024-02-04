pdata = """Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
Cupid can fly 8 km/s for 17 seconds, but then must rest for 114 seconds.
Prancer can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Donner can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 11 km/s for 12 seconds, but then must rest for 125 seconds.
Comet can fly 21 km/s for 6 seconds, but then must rest for 121 seconds.
Blitzen can fly 18 km/s for 3 seconds, but then must rest for 50 seconds.
Vixen can fly 20 km/s for 4 seconds, but then must rest for 75 seconds.
Dancer can fly 7 km/s for 20 seconds, but then must rest for 119 seconds."""

tdata = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds"""


def part2(data: str, debug: bool = False):
    if data == tdata:
        seconds = 1000
    else:
        seconds = 2503

    reindeer = []
    for line in data.splitlines():
        words = line.split()
        reindeer.append([int(words[3]), int(words[6]), int(words[13]), int(words[6]), 0, 0])

    # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds

    points = [0] * len(reindeer)

    for second in range(seconds):
        for r in reindeer:
            if r[3] > 0:
                r[5] += r[0]
                r[3] = r[3] - 1
                if r[3] == 0:
                    r[4] = r[2]
            else:
                r[4] = r[4] - 1
                if r[4] == 0:
                    r[3] = r[1]

        current_winner = reindeer[0][5]
        current_winner_index = 0
        for idx, r in enumerate(reindeer[1:], start=1):
            if r[5] > current_winner:
                current_winner = r[5]
                current_winner_index = idx
        points[current_winner_index] += 1

    current_winner = reindeer[0][5]
    current_winner_index = 0
    for idx, r in enumerate(reindeer[1:], start=1):
        if r[5] > current_winner:
            current_winner = r[5]
            current_winner_index = idx
    points[current_winner_index] += 1

    if debug:
        print(reindeer)

    print(max(points))


def part1(data: str, debug: bool = False):
    if data == tdata:
        seconds = 1000
    else:
        seconds = 2503

    reindeer = []
    for line in data.splitlines():
        words = line.split()
        reindeer.append([int(words[3]), int(words[6]), int(words[13]), int(words[6]), 0, 0])

    # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds

    for second in range(seconds):
        for r in reindeer:
            if r[3] > 0:
                r[5] += r[0]
                r[3] = r[3] - 1
                if r[3] == 0:
                    r[4] = r[2]
            else:
                r[4] = r[4] - 1
                if r[4] == 0:
                    r[3] = r[1]

    if debug:
        print(reindeer)

    print(max(r[5] for r in reindeer))


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
