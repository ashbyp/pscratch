from algorithms.aoc.utils import read_file

pdata = read_file('data/8_puzzle.txt')

tdata = read_file('data/8_test.txt')


def part2(data: str, debug: bool = False):
    total_chars, expanded_chars = 0, 0
    for line in data.splitlines():
        line_len = len(line)
        total_chars += line_len
        idx = 0
        expand = 2

        while idx != line_len:
            if line[idx] == '"':
                expand += 2
            elif line[idx] == '\\':
                expand += 2
            else:
                expand += 1
            idx += 1
        expanded_chars += expand

        if debug:
            print(line, expand)

    print('Total chars: ', total_chars, 'Expanded chars: ', expanded_chars, 'Diff: ', expanded_chars - total_chars)


def part1(data: str, debug: bool = False):
    total_chars, total_mem = 0, 0
    for line in data.splitlines():
        line_len = len(line)
        total_chars += line_len
        idx = 0
        mem = 0
        esc = False

        while idx != line_len:
            if esc:
                if line[idx] == 'x':
                    idx += 2
                mem += 1
                esc = False
            else:
                if line[idx] == '\\':
                    esc = True
                elif line[idx] != '"':
                    mem += 1
            idx += 1
        total_mem += mem

    print('Total chars: ', total_chars, 'Total mem: ', total_mem, 'Diff: ', total_chars - total_mem)


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
