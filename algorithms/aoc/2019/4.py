pdata = """206938-679128"""

tdata = """111111
223450
123789
112233
123444
111122"""

tdata = '111122'


def is_valid(pword):
    """
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever
    increase or stay the same (like 111123 or 135679).
    """
    if len(pword) != 6: return False
    same = False
    for i in range(1, 6):
        if pword[i - 1] == pword[i]: same = True
        if int(pword[i]) < int(pword[i - 1]): return False
    return same


def is_valid2(pword):
    if len(pword) != 6: return False
    same = 1
    sames = set()
    for i in range(1, 6):
        if pword[i - 1] == pword[i]:
            same += 1
        else:
            sames.add(same)
            same = 1
        if int(pword[i]) < int(pword[i - 1]):
            return False

    sames.add(same)

    return 2 in sames


def part2(data):
    if '-' in data:
        start, end = data.split('-')
        count = 0
        for i in range(int(start), int(end) + 1):
            if is_valid2(str(i)): count += 1
        print(count)
    else:
        for line in data.splitlines():
            print(line, is_valid2(line))


def part1(data):
    if '-' in data:
        start, end = data.split('-')
        count = 0
        for i in range(int(start), int(end) + 1):
            if is_valid(str(i)): count += 1
        print(count)
    else:
        for line in data.splitlines():
            print(line, is_valid(line))


if __name__ == '__main__':
    def run(m, d, f):
        if d:
            print(f'{m:15} ------------')
            f(d)
            print()

    # 1653 and 1133

    run("Part 1 test", tdata, part1)
    run("Part 1 puzzle", pdata, part1)
    run("Part 2 test", tdata, part2)
    run("Part 2 puzzle", pdata, part2)
