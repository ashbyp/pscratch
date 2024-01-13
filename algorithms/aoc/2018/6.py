pdata = """59, 110
127, 249
42, 290
90, 326
108, 60
98, 168
358, 207
114, 146
242, 170
281, 43
233, 295
213, 113
260, 334
287, 260
283, 227
328, 235
96, 259
232, 177
198, 216
52, 115
95, 258
173, 191
156, 167
179, 135
235, 235
164, 199
248, 180
165, 273
160, 297
102, 96
346, 249
176, 263
140, 101
324, 254
72, 211
126, 337
356, 272
342, 65
171, 295
93, 192
47, 200
329, 239
60, 282
246, 185
225, 324
114, 329
134, 167
212, 104
338, 332
293, 94"""

tdata = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""


def part2(data: str, debug=False):
    limit = 32 if data == tdata else 10000
    points = []
    for line in data.splitlines():
        points.append(tuple(map(int, line.split(','))))

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    size = 0

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 2):
            pt = (x, y)
            sum_man_dist = sum([m_dist(pt, p)[0] for p in points])
            if sum_man_dist < limit:
                size += 1

    print(size)


def m_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), p2


def part1(data: str, debug=False):
    from collections import Counter
    points = []
    for line in data.splitlines():
        points.append(tuple(map(int, line.split(','))))
    print(points)
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    print(min_x, max_x, min_y, max_y)

    mins = []
    res = [[None for _ in range(max_y + 1)] for _ in range(max_x + 2)]

    if debug:
        for y in range(max_y + 1):
            for x in range(max_x + 2):
                print((x, y), ' ', end='')
            print()

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 2):
            pt = (x, y)
            man_dists = sorted([m_dist(pt, p) for p in points])
            if debug:
                print(pt)
                print('  Man dists', man_dists)
            if man_dists[0][0] != man_dists[1][0]:
                mins.append(man_dists[0][1])
                res[x][y] = man_dists[0][1]

    if debug:
        print('Min ', mins)

    if debug:
        labels = {
            (1, 1): 'a', (1, 6): 'b', (8, 3): 'c', (3, 4): 'd', (5, 5): 'e', (8, 9): 'f'
        }

        for y in range(max_y + 1):
            for x in range(max_x + 2):
                if (x, y) in labels:
                    print(labels[(x, y)].upper(), ' ', end='')
                else:
                    print(labels[res[x][y]] if res[x][y] else '.', ' ', end='')
            print()

    cleaned = []
    removed = set()
    for p in mins:
        if p[0] in (min_x, max_x) or p[1] in (min_y, max_y):
            if debug:
                removed.add(labels[p])
        else:
            cleaned.append(p)

    if debug:
        print('Removed ', removed)
        print('Cleaned ', cleaned)

    print(Counter(cleaned))


if __name__ == '__main__':
    def run(m, d, f):
        if d:
            print(f'{m:15} ------------')
            f(d)
            print()


    run("Part 1 test", tdata, part1)
    run("Part 1 puzzle", pdata, part1)
    run("Part 2 test", tdata, part2)
    run("Part 2 puzzle", pdata, part2)
