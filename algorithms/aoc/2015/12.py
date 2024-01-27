from algorithms.aoc.utils import read_file

pdata = read_file("data/12_puzzle.txt")

tdata = """"""


def part2(data: str, debug: bool = False):
    import json
    data = json.loads(data)

    total = [0]

    def count(element):
        if isinstance(element, dict):
            if 'red' not in element and 'red' not in element.values():
                for v in element.values():
                    count(v)
        elif isinstance(element, list):
            for e in element:
                count(e)
        elif isinstance(element, str):
            pass
        else:
            total[0] = total[0] + element

    count(data)
    print(total)


def part1(data: str, debug: bool = False):
    import json
    data = json.loads(data)

    total = [0]

    def count(element):
        if isinstance(element, dict):
            for v in element.values():
                count(v)
        elif isinstance(element, list):
            for e in element:
                count(e)
        elif isinstance(element, str):
            pass
        else:
            total[0] = total[0] + element

    count(data)
    print(total)


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
