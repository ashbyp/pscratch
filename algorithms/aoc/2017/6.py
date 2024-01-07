pdata = """11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"""

tdata = """0 2 7 0"""


def get_max(banks: list[int]) -> int:
    m = 0
    mi = 0
    for i in range(len(banks)):
        if banks[i] > m:
            mi = i
            m = banks[i]
    return mi


def part2(data: str):
    banks = list(map(int, data.split()))
    n_banks = len(banks)
    arrangement = int(''.join(map(str, banks)))
    arrangements = {arrangement}
    num_arrangements = 0

    # print(f'Start Banks={banks}')

    check_cycle = None

    while True:
        max_b = get_max(banks)
        to_dist = banks[max_b]
        banks[max_b] = 0

        for i in range(max_b + 1, max_b + to_dist + 1):
            banks[i % n_banks] = banks[i % n_banks] + 1
        num_arrangements += 1
        arrangement = int(''.join(map(str, banks)))
        if check_cycle and check_cycle == arrangement:
            break
        else:
            if arrangement in arrangements:
                if not check_cycle:
                    check_cycle = arrangement
                    num_arrangements = 0
        arrangements.add(arrangement)

    print(f'Banks={banks}, {num_arrangements}')


def part1(data: str):
    banks = list(map(int, data.split()))
    n_banks = len(banks)
    arrangement = int(''.join(map(str, banks)))
    arrangements = {arrangement}
    num_arrangements = 0

    # print(f'Start Banks={banks}')

    while True:
        max_b = get_max(banks)
        to_dist = banks[max_b]
        # print(f'  Max {max_b}, Dist{to_dist}')

        banks[max_b] = 0
        for i in range(max_b + 1, max_b + to_dist + 1):
            banks[i % n_banks] = banks[i % n_banks] + 1
        num_arrangements += 1
        arrangement = int(''.join(map(str, banks)))
        if arrangement in arrangements:
            break
        arrangements.add(arrangement)

    print(f'Banks={banks}, {num_arrangements}')


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
