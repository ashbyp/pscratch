pdata = """cqjxjnds"""

tdata = """"""


def next_poss(passwd: list[str]) -> list[str]:
    p = len(passwd) - 1
    while passwd[p] == 'z':
        passwd[p] = 'a'
        p -= 1
    if p == -1:
        p = len(passwd) - 1
    passwd[p] = chr(ord(passwd[p]) + 1)
    return passwd


def check1(passwd: list[str]) -> bool:
    """Passwords must include one increasing straight of at least
    three letters, like abc, bcd, cde, and so on, up to xyz. They cannot
    skip letters; abd doesn't count.
    """
    count = 1
    last = ord(passwd[0])
    for s in passwd[1:]:
        o = ord(s)
        if o - last == 1:
            count += 1
            if count == 3: return True
        else:
            count = 1
        last = o
    return False


def check2(passwd: list[str]) -> bool:
    """Passwords may not contain the letters i, o, or l, as these letters can
    be mistaken for other characters and are therefore confusing.
    """
    for s in passwd:
        if s in ('i', 'o', 'l'):
            return False
    return True


def check3(passwd: list[str]) -> bool:
    """Passwords must contain at least two different, non-overlapping
    pairs of letters, like aa, bb, or zz.
    """
    pairs = set()
    last = passwd[0]
    for s in passwd[1:]:
        if s == last:
            pairs.add(last)
        else:
            last = s
    return len(pairs) > 1


def part2(data: str, debug: bool = False):
    passwd = list(data)
    while not all([check1(passwd), check2(passwd), check3(passwd)]):
        passwd = next_poss(passwd)
    passwd = next_poss(passwd)
    while not all([check1(passwd), check2(passwd), check3(passwd)]):
        passwd = next_poss(passwd)
    print(''.join(passwd))


def part1(data: str, debug: bool = False):
    passwd = list(data)
    while not all([check1(passwd), check2(passwd), check3(passwd)]):
        passwd = next_poss(passwd)
    print(''.join(passwd))


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
