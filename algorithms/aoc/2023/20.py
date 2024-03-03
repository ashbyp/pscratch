question = "https://adventofcode.com/2023/day/20"
input_data = "https://adventofcode.com/2023/day/20/input"

pdata = """%dm -> jz, ct
&ft -> rx
%hc -> kh
%kg -> gd, sl
&sl -> bs, bq, ts, zd, gk, xx, lp
%rf -> xk, jz
%zd -> kg
%dp -> ql, pq
%ss -> pq, mb
&rr -> hc, lt, kh, fv, tc, vg
%hv -> nh
%nh -> pq, xm
&jz -> bn, vz, xz
%vf -> nc, sl
%gk -> pc
%bs -> gk
&pq -> tb, qh, ls, hv, ql
%jb -> rr, hc
%fv -> cd, rr
&vz -> ft
%mm -> jr, rr
%vg -> mm
%cd -> tc, rr
&bq -> ft
%xg -> pb, jz
%xx -> zd
%ls -> tb, pq
%pb -> jz, rz
%tc -> vp
%kh -> ck
%lp -> xx
%tb -> ss
%qk -> jz, xg
%xz -> dm
%jr -> rb, rr
%mb -> hv, pq
&qh -> ft
&lt -> ft
%rb -> rr
%pc -> hr, sl
%hr -> vf, sl
%gd -> bs, sl
%xm -> dp, pq
%ct -> jz, rj
%ck -> vg, rr
%cr -> jz, rf
%bn -> xz, jz
%vp -> rr, jb
%hl -> pq, vj
%ts -> lp, sl
%rz -> jz, cr
%ql -> tr
%xk -> jz
%vj -> pq
%tr -> pq, hl
broadcaster -> ls, fv, ts, bn
%nc -> sl
%rj -> jz, qk"""

tdata = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

FEEDERS = {'vz': None, 'bq': None, 'qh': None, 'lt': None}


def rx(nodes, graph, debug, button):
    signals = [('broadcaster', 0, n) for n in graph['broadcaster']]

    while signals:
        new_signals = []
        if debug:
            print('Signals', signals)

        for from_node_name, sig, node_name in signals:
            if from_node_name in FEEDERS.keys() and sig == 1 and FEEDERS[from_node_name] is None:
                print(" high pulse at feeder -> ", from_node_name, sig, button)
                FEEDERS[from_node_name] = button
                if all(FEEDERS.values()):
                    import math
                    print("Poss answer ", math.lcm(*FEEDERS.values()))

            if node_name not in nodes:
                if node_name == 'rx' and sig == 0:
                    return True
                continue

            node = nodes[node_name]
            targets = graph[node_name]
            if node[0] == '%':
                if sig == 1:
                    continue
                else:
                    node[2] = not node[2]
                    pulse = 1 if node[2] else 0
                    for t in targets:
                        new_signals.append((node_name, pulse, t))
            elif node[0] == '&':
                node[1][from_node_name] = sig
                if all(x == 1 for x in node[1].values()):
                    pulse = 0
                else:
                    pulse = 1
                for t in targets:
                    new_signals.append((node_name, pulse, t))
            else:
                for t in targets:
                    new_signals.append((node_name, sig, t))

        signals = new_signals

    return False


def part2(data: str, debug: bool = False):
    from collections import defaultdict
    graph = defaultdict(list)
    nodes = {}
    for line in data.splitlines():
        bef, aft = line.split(' -> ')
        if bef[0] in ('%', '&'):
            name = bef[1:]
            node = [bef[0], {}, False]
        else:
            name = bef
            node = [None, {}, False]
        nodes[name] = node
        for n in aft.split(', '):
            graph[name].append(n)

    cons = defaultdict(list)
    for k, v in nodes.items():
        if v[0] == '&':
            cons[k] = []
    for k, v in graph.items():
        for c in cons:
            if c in v:
                cons[c].append(k)

    for c, values in cons.items():
        nodes[c][1] = dict((v, 0) for v in values)

    for b in range(1, 100000000):
        if rx(nodes, graph, debug, b):
            print(b)
            break


def broadcast(nodes, graph, debug):
    high, low = 0, 0

    signals = [('broadcaster', 0, n) for n in graph['broadcaster']]

    low += len(signals) + 1

    while signals:
        new_signals = []
        if debug:
            print('Signals', signals)

        for from_node_name, sig, node_name in signals:
            if not node_name in nodes:
                continue

            node = nodes[node_name]
            targets = graph[node_name]
            # if debug:
            #     print(node, targets)
            if node[0] == '%':
                if sig == 1:
                    continue
                else:
                    node[2] = not node[2]
                    pulse = 1 if node[2] else 0
                    for t in targets:
                        new_signals.append((node_name, pulse, t))
                    if pulse:
                        high += len(targets)
                    else:
                        low += len(targets)
            elif node[0] == '&':
                node[1][from_node_name] = sig
                if all(x == 1 for x in node[1].values()):
                    pulse = 0
                else:
                    pulse = 1
                for t in targets:
                    new_signals.append((node_name, pulse, t))
                if pulse:
                    high += len(targets)
                else:
                    low += len(targets)
            else:
                for t in targets:
                    new_signals.append((node_name, sig, t))
                if sig:
                    high += len(targets)
                else:
                    low += len(targets)

        signals = new_signals

    return high, low


def part1(data: str, debug: bool = False):
    from collections import defaultdict
    graph = defaultdict(list)
    nodes = {}
    for line in data.splitlines():
        bef, aft = line.split(' -> ')
        if bef[0] in ('%', '&'):
            name = bef[1:]
            node = [bef[0], {}, False]
        else:
            name = bef
            node = [None, {}, False]
        nodes[name] = node
        for n in aft.split(', '):
            graph[name].append(n)

    cons = defaultdict(list)
    for k, v in nodes.items():
        if v[0] == '&':
            cons[k] = []
    for k, v in graph.items():
        for c in cons:
            if c in v:
                cons[c].append(k)

    for c, values in cons.items():
        nodes[c][1] = dict((v, 0) for v in values)

    if debug:
        print(nodes)
        print(graph)

    high, low, num = 0, 0, 1000

    for _ in range(num):
        h, l = broadcast(nodes, graph, debug)
        high += h
        low += l

    print(h, l)
    print(high * low)


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
    # run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
