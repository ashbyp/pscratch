question = "https://adventofcode.com/2024/day/8"
input_data = "https://adventofcode.com/2024/day/8/input"

pdata = """.............C.7..................G..0...y........
..................7................C..............
....................................0......W....y.
.......................................D..W.......
..........u.......................................
..................................4.......D0...j..
.....................................D............
................O.....C................G..........
............F.....................C...............
......u..........F.................4.......y......
..........X..........5....4...........1...........
..........F...........5X...................3......
.............F.............................j.3....
.................u..............X.................
............................7.....................
..................................................
..........................5.....j2.........4......
....d.....................y...................j1..
..................................................
............................Y.e...................
.................d...X...............J...........e
.............d....................................
..............................Y..............1....
.........................................Y........
......................W......8..f...J.........3...
.......w.............J............................
...................................U.....f......e.
.................................Of....e....t...1.
.......g..........d......s........................
................G................f................
.....................................O............
...g........................T.....U...............
......................s..........T.............G..
................................s.......8.........
.....9........g...........o...U............E......
............g............................t....o...
...........................................6....E.
.....................s......x........6....E.......
..........w.9................x............t.......
...........9........w...........J.....6o..........
.............................................o....
..........S................U......................
.......S..2..........c........T.O....t............
.....2...S.....c...................T..............
..................x.......................8.......
....9.............................................
...wS.....................................6.......
................2........................8........
..................................................
.................x....c........................E.."""

tdata = """..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
.........."""

# tdata = """..........
# ..........
# .....a....
# ....a.....
# ..........
# ..........
# ..........
# ..........
# ..........
# .........."""

tdata="""T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""

tdata="""............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def draw_grid(grid, n_rows, n_cols, anti_nodes=None):
    overrides = anti_nodes if anti_nodes else set()

    for r in range(n_rows):
        for c in range(n_cols):
            if (r, c) in overrides:
                print('#', end='')
            else:
                print(grid[r][c], end='')
        print()


def in_grid(r, c, n_rows, n_cols):
    return 0 <= r < n_rows and 0 <= c < n_cols


def part2(data: str, _debug: bool = False):
    grid = [list(line) for line in data.splitlines()]
    n_rows = len(grid)
    n_cols = len(grid[0])

    if _debug:
        draw_grid(grid, n_rows, n_cols)

    from collections import defaultdict
    antennas = defaultdict(list)
    anti_nodes = set()

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]].append((r, c))
                anti_nodes.add((r, c))

    if _debug:
        print(antennas)



    from itertools import combinations

    for A in antennas:
        pts = antennas[A]
        if _debug:
            print('Processing', pts)
        for a, b in combinations(pts, 2):
            dr, dc = abs(a[0] - b[0]), abs(a[1] - b[1])
            if _debug:
                print('  Processing pair', a, b, 'dr=', dr, 'dc=', dc)

            i = 1
            while True:
                if b[1] >= a[1]:
                    if _debug:
                        print('Down right')
                    p1 = a[0] - dr * i, a[1] - dc * i
                    p2 = b[0] + dr * i, b[1] + dc * i
                else:
                    if _debug:
                        print('Down left')
                    p1 = a[0] - dr * i, a[1] + dc * i
                    p2 = b[0] + dr * i, b[1] - dc * i

                if _debug:
                    print('  Anti nodes', p1, p2)

                added = False
                if in_grid(*p1, n_rows, n_cols):
                    anti_nodes.add(p1)
                    added = True
                if in_grid(*p2, n_rows, n_cols):
                    anti_nodes.add(p2)
                    added = True

                if not added: break

                i += 1

            if _debug: draw_grid(grid, n_rows, n_cols, anti_nodes)

    if _debug:
        print('Final anti nodes: ', anti_nodes)

    print(len(anti_nodes))


def part1(data: str, _debug: bool = False):
    grid = [list(line) for line in data.splitlines()]
    n_rows = len(grid)
    n_cols = len(grid[0])

    if _debug:
        draw_grid(grid, n_rows, n_cols)

    from collections import defaultdict
    antennas = defaultdict(list)

    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]].append((r, c))

    if _debug:
        print(antennas)

    anti_nodes = set()

    from itertools import combinations

    for A in antennas:
        pts = antennas[A]
        if _debug:
            print('Processing', pts)
        for a, b in combinations(pts, 2):
            dr, dc = abs(a[0] - b[0]), abs(a[1] - b[1])
            if _debug:
                print('  Processing pair', a, b, 'dr=', dr, 'dc=', dc)

            if b[1] >= a[1]:
                if _debug:
                    print('Down right')
                p1 = a[0] - dr, a[1] - dc
                p2 = b[0] + dr, b[1] + dc
            else:
                if _debug:
                    print('Down left')
                p1 = a[0] - dr, a[1] + dc
                p2 = b[0] + dr, b[1] - dc

            if _debug:
                print('  Anti nodes', p1, p2)

            if in_grid(*p1, n_rows, n_cols): anti_nodes.add(p1)
            if in_grid(*p2, n_rows, n_cols): anti_nodes.add(p2)

            if _debug: draw_grid(grid, n_rows, n_cols, anti_nodes)

    if _debug:
        print('Final anti nodes: ', anti_nodes)

    print(len(anti_nodes))


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    run("Part 1 test", tdata, part1, False)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, False)
    run("Part 2 puzzle", pdata, part2, False)

    # 14 222 34 884


if __name__ == '__main__':
    main()
