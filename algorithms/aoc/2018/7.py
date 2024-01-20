pdata = """Step O must be finished before step C can begin.
Step Y must be finished before step D can begin.
Step N must be finished before step D can begin.
Step G must be finished before step F can begin.
Step C must be finished before step Z can begin.
Step H must be finished before step K can begin.
Step W must be finished before step T can begin.
Step T must be finished before step F can begin.
Step S must be finished before step I can begin.
Step X must be finished before step B can begin.
Step J must be finished before step A can begin.
Step K must be finished before step D can begin.
Step Z must be finished before step A can begin.
Step A must be finished before step B can begin.
Step L must be finished before step V can begin.
Step F must be finished before step M can begin.
Step B must be finished before step V can begin.
Step M must be finished before step Q can begin.
Step D must be finished before step E can begin.
Step I must be finished before step U can begin.
Step R must be finished before step V can begin.
Step E must be finished before step U can begin.
Step P must be finished before step V can begin.
Step V must be finished before step Q can begin.
Step U must be finished before step Q can begin.
Step P must be finished before step U can begin.
Step O must be finished before step F can begin.
Step T must be finished before step M can begin.
Step I must be finished before step Q can begin.
Step M must be finished before step U can begin.
Step R must be finished before step E can begin.
Step T must be finished before step R can begin.
Step H must be finished before step S can begin.
Step L must be finished before step B can begin.
Step S must be finished before step Q can begin.
Step E must be finished before step Q can begin.
Step B must be finished before step Q can begin.
Step S must be finished before step M can begin.
Step C must be finished before step D can begin.
Step S must be finished before step R can begin.
Step G must be finished before step D can begin.
Step T must be finished before step E can begin.
Step T must be finished before step Q can begin.
Step N must be finished before step I can begin.
Step S must be finished before step P can begin.
Step N must be finished before step J can begin.
Step X must be finished before step L can begin.
Step G must be finished before step K can begin.
Step N must be finished before step E can begin.
Step H must be finished before step D can begin.
Step H must be finished before step P can begin.
Step O must be finished before step A can begin.
Step V must be finished before step U can begin.
Step F must be finished before step D can begin.
Step B must be finished before step P can begin.
Step T must be finished before step L can begin.
Step I must be finished before step P can begin.
Step K must be finished before step Z can begin.
Step G must be finished before step M can begin.
Step F must be finished before step Q can begin.
Step J must be finished before step L can begin.
Step H must be finished before step Q can begin.
Step W must be finished before step R can begin.
Step R must be finished before step U can begin.
Step P must be finished before step Q can begin.
Step D must be finished before step V can begin.
Step G must be finished before step C can begin.
Step Z must be finished before step B can begin.
Step O must be finished before step H can begin.
Step S must be finished before step A can begin.
Step J must be finished before step Q can begin.
Step N must be finished before step F can begin.
Step L must be finished before step R can begin.
Step O must be finished before step R can begin.
Step W must be finished before step M can begin.
Step J must be finished before step F can begin.
Step G must be finished before step W can begin.
Step K must be finished before step U can begin.
Step D must be finished before step U can begin.
Step W must be finished before step I can begin.
Step E must be finished before step V can begin.
Step Y must be finished before step Q can begin.
Step L must be finished before step E can begin.
Step S must be finished before step B can begin.
Step T must be finished before step V can begin.
Step C must be finished before step U can begin.
Step M must be finished before step P can begin.
Step G must be finished before step S can begin.
Step B must be finished before step R can begin.
Step K must be finished before step M can begin.
Step X must be finished before step A can begin.
Step R must be finished before step P can begin.
Step B must be finished before step I can begin.
Step C must be finished before step X can begin.
Step O must be finished before step P can begin.
Step D must be finished before step Q can begin.
Step F must be finished before step B can begin.
Step I must be finished before step R can begin.
Step Y must be finished before step I can begin.
Step M must be finished before step D can begin.
Step F must be finished before step U can begin."""
tdata = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""


def part2(data: str, debug: bool = False):
    # on desk at work
    pass


def part1(data: str, debug: bool = False):
    from collections import defaultdict
    graph = defaultdict(list)
    all_nodes = set()
    for line in data.splitlines():
        line = line.split()
        bef, aft = line[1], line[7]
        graph[aft].append(bef)
        all_nodes.add(bef)
        all_nodes.add(aft)
    poss = list(set(all_nodes).difference(graph.keys()))

    res = ''
    while poss:
        poss = sorted(poss)
        cur = poss[0]
        res += cur
        poss.remove(cur)
        for node, prereqs in graph.items():
            if prereqs:
                if cur in prereqs:
                    prereqs.remove(cur)
                if len(prereqs) == 0 and node not in poss:
                    poss.append(node)

    print(res)


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
