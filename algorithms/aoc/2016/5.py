pdata = """uqwqemis"""

tdata = """abc"""

import hashlib

def part2(data: str):
    pword = ['_' for _ in range(8)]
    found = 0
    extra = 0
    while found != 8:
        extra += 1
        s = data + str(extra)
        s = s.encode("utf-8")
        h = hashlib.md5(s).hexdigest()
        if h.startswith("00000"):
            if h[5].isdigit():
                pos = int(h[5])
                if (0 <= pos < 8) and pword[pos] == '_':
                    ch = h[6]
                    pword[pos] = ch
                    print(''.join(pword))
    print(''.join(pword))

def part1(data: str):
    pword = ''
    extra = 0
    while len(pword) != 8:
        extra += 1
        s = data + str(extra)
        s = s.encode("utf-8")
        h = hashlib.md5(s).hexdigest()
        if h.startswith("00000"):
            pword += h[5]
            print(pword)
    print(pword)


if __name__ == '__main__':
    def run(m, d, f):
        if d:
            print(f'{m:15} ------------')
            f(d)
            print()


    # run("Part 1 test", tdata, part1)
    # run("Part 1 puzzle", pdata, part1)
    # run("Part 2 test", tdata, part2)
    run("Part 2 puzzle", pdata, part2)
