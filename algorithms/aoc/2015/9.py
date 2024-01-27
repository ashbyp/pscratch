pdata = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46"""

tdata = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""


def part2(data: str, debug: bool = False):
    from collections import defaultdict
    from itertools import permutations
    routes = defaultdict(dict)
    all_cities = set()

    for line in data.splitlines():
        words = line.split()
        routes[words[0]][words[2]] = int(words[4])
        routes[words[2]][words[0]] = int(words[4])
        all_cities.add(words[0])
        all_cities.add(words[2])

    if debug:
        print(routes)

    longest = float('-inf')

    for perm in permutations(all_cities):
        if debug:
            print(perm)
        d = 0
        for i in range(0, len(perm) - 1):
            if perm[i] in routes:
                if perm[i + 1] in routes[perm[i]]:
                    d += routes[perm[i]][perm[i + 1]]
                else:
                    if debug:
                        print(perm[i], ' to ', perm[i + 1], 'not found')
                    break
            else:
                if debug:
                    print(perm[i], ' not in routes')
                break
        else:
            if debug:
                print(perm, d)

            longest = max(d, longest)

    print(longest)


def part1(data: str, debug: bool = False):
    from collections import defaultdict
    from itertools import permutations
    routes = defaultdict(dict)
    all_cities = set()

    for line in data.splitlines():
        words = line.split()
        routes[words[0]][words[2]] = int(words[4])
        routes[words[2]][words[0]] = int(words[4])
        all_cities.add(words[0])
        all_cities.add(words[2])

    if debug:
        print(routes)

    shortest = float('inf')

    for perm in permutations(all_cities):
        if debug:
            print(perm)
        d = 0
        for i in range(0, len(perm) - 1):
            if perm[i] in routes:
                if perm[i + 1] in routes[perm[i]]:
                    d += routes[perm[i]][perm[i+1]]
                else:
                    if debug:
                        print(perm[i], ' to ', perm[i+1], 'not found')
                    break
            else:
                if debug:
                    print(perm[i], ' not in routes')
                break
        else:
            if debug:
                print(perm, d)

            shortest = min(d, shortest)

    print(shortest)

def main():
    import timeit

    def run(msg, data, fn, debug):
        if data or True:
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
