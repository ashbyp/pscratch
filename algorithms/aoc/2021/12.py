question = "https://adventofcode.com/2021/day/12"
input_data = "https://adventofcode.com/2021/day/12/input"

pdata = """zs-WO
zs-QJ
WO-zt
zs-DP
WO-end
gv-zt
iu-SK
HW-zs
iu-WO
gv-WO
gv-start
gv-DP
start-WO
HW-zt
iu-HW
gv-HW
zs-SK
HW-end
zs-end
DP-by
DP-iu
zt-start"""

tdata = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

tdata1="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


def part2(data: str, debug: bool = False):
    from collections import defaultdict
    graph = defaultdict(list)
    for line in data.splitlines():
        left, right = line.split('-')
        graph[left].append(right)
        if left == 'start' or right == 'end':
            pass
        else:
            graph[right].append(left)
    if debug:
        print(graph)

    paths = []

    def find(path, cond):
        if path[-1] == 'end':
            paths.append(path)
            return
        if debug:
            # print('at node ', path[-1], ' trying ', graph[path[-1]])
            pass
        for nex in graph[path[-1]]:
            if nex.isupper():
                find(path + [nex], cond)
            else:
                if nex == 'start':
                    pass
                elif nex not in path:
                    find(path + [nex], cond)
                else:
                    if not cond:
                        find(path + [nex], True)

    find(['start'], False)

    if debug:
        print(paths)

    print(len(paths))


def part1(data: str, debug: bool = False):
    from collections import defaultdict
    graph = defaultdict(list)
    for line in data.splitlines():
        left, right = line.split('-')
        graph[left].append(right)
        if not(left == 'start' or right == 'end'):
            graph[right].append(left)
    if debug:
        print(graph)

    paths = []

    def find(path):
        if path[-1] == 'end':
            paths.append(path)
            return
        if debug:
            print('at node ', path[-1], ' trying ', graph[path[-1]])

        for nex in graph[path[-1]]:
            if nex.isupper():
                find(path + [nex])
            else:
                if nex not in path:
                    find(path + [nex])
    find(['start'])

    if debug:
        print(paths)

    print(len(paths))


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
    run("Part 2 test", tdata1, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
