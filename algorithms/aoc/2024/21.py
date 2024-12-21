import functools

from pandas.core.computation.align import reconstruct_object

question = "https://adventofcode.com/2024/day/9"
input_data = "https://adventofcode.com/2024/day/9/input"

pdata = """140A
170A
169A
803A
129A"""

# pdata = """"""

tdata = """029A"""

_NPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '-1': (3, 0), '0': (3, 1), 'A': (3, 2)
}

_DPAD = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
    '-1': (0, 0)
}

DIRS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

NPAD = 1
DPAD = 2

@functools.cache
def generate_sequence(start, end, type):
    if start == end:
        return ''

    print('X')

    if type == NPAD: coordinates = _NPAD
    else: coordinates = _DPAD

    no_go = coordinates['-1']

    start_coord = coordinates[start]
    end_coord = coordinates[end]

    sequence = []

    while start_coord[1] < end_coord[1]:  # Move right
        sequence.append('>')
        start_coord = (start_coord[0], start_coord[1] + 1)
    while start_coord[0] < end_coord[0]:  # Move down
        sequence.append('v')
        start_coord = (start_coord[0] + 1, start_coord[1])
    while start_coord[0] > end_coord[0]:  # Move up
        sequence.append('^')
        start_coord = (start_coord[0] - 1, start_coord[1])
    while start_coord[1] > end_coord[1]:  # Move left
        sequence.append('<')
        start_coord = (start_coord[0], start_coord[1] - 1)

    sorted_seqennce = sorted(sequence)
    r, c = coordinates[start]
    for s in sorted_seqennce:
        r, c = r + DIRS[s][0], c + DIRS[s][1]
        if (r, c) == no_go:
            return ''.join(sequence)

    return ''.join(sorted_seqennce)

@functools.cache
def robot(seq):

    print('len', len(seq))

    res = ''
    seq = 'A' + seq
    for j in range(0, len(seq) - 1):
        res += generate_sequence(seq[j], seq[j + 1], DPAD) + 'A'
    return res

def part2(data: str, _debug: bool = False):


    tot = 0
    for code in data.splitlines():

        code = 'A' + code
        print(code)

        robot_seq = ''

        for i in range(0, len(code) - 1):
            code_seq = generate_sequence(code[i], code[i + 1], NPAD) + 'A'

            x = code_seq

            for X in range(25):
                if X == 15:
                    print('here')
                x = robot(x)
                print(X, end=',')
            print()

            robot_seq += x

        print(robot_seq)

        code = int(code.lstrip('0').replace('A', ''))
        l = len(robot_seq)
        tot += l * code

    print('Total', tot)


def part1(data: str, _debug: bool = False):
    tot = 0
    for code in data.splitlines():
        num_seq = ''
        robot_seq = ''
        robot1_seq = ''

        code = 'A' + code
        for i in range(0, len(code) - 1):
            seq = generate_sequence(code[i], code[i + 1], NPAD) + 'A'
            num_seq += seq
            seq = 'A' + seq
            for j in range(0, len(seq) - 1):
                rseq = generate_sequence(seq[j], seq[j + 1], DPAD) + 'A'
                robot_seq += rseq
                rseq = 'A' + rseq
                for k in range(0, len(rseq) - 1):
                    robot1_seq += generate_sequence(rseq[k], rseq[k + 1], DPAD) + 'A'

        print('code', code)
        print('num ', num_seq)
        print('rob1', robot_seq)
        print('rob2', robot1_seq)
        print('len:', len(robot1_seq))

        code = int(code.lstrip('0').replace('A', ''))
        l = len(robot1_seq)
        print(f'{l} * {code} = {l * code}')
        tot += l * code

    print('Total', tot)


def main():
    import timeit

    def run(msg, data, fn, debug):
        if data:
            print(f'*** {msg:13} ---------------')
            start = timeit.default_timer()
            fn(data, debug)
            elapsed_ms = (timeit.default_timer() - start) * 1000
            print(f'Time {elapsed_ms:.10f} ms ------------')

    # run("Part 1 test", tdata, part1, True)
    # run("Part 1 puzzle", pdata, part1, False)  # 105458
    # run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()

i = '>vA^<<AA>Av<AAA>^A'
j = 'vA<^AA>A<vAAA>^A'
