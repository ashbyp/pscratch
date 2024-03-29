question = "https://adventofcode.com/2021/day/14"
input_data = "https://adventofcode.com/2021/day/14/input"

pdata = """NBOKHVHOSVKSSBSVVBCS

SN -> H
KP -> O
CP -> V
FN -> P
FV -> S
HO -> S
NS -> N
OP -> C
HC -> S
NP -> B
CF -> V
NN -> O
OS -> F
VO -> V
HK -> N
SV -> V
VC -> V
PH -> K
NH -> O
SB -> N
KS -> V
CB -> H
SS -> P
SP -> H
VN -> K
VP -> O
SK -> V
VF -> C
VV -> B
SF -> K
HH -> K
PV -> V
SO -> H
NK -> P
NO -> C
ON -> S
PB -> K
VS -> H
SC -> P
HS -> P
BS -> P
CS -> P
VB -> V
BP -> K
FH -> O
OF -> F
HF -> F
FS -> C
BN -> O
NC -> F
FC -> B
CV -> V
HN -> C
KF -> K
OO -> P
CC -> S
FF -> C
BC -> P
PP -> F
KO -> V
PC -> B
HB -> H
OB -> N
OV -> S
KH -> B
BO -> B
HV -> P
BV -> K
PS -> F
CH -> C
SH -> H
OK -> V
NB -> K
BF -> S
CO -> O
NV -> H
FB -> K
FO -> C
CK -> P
BH -> B
OH -> F
KB -> N
OC -> K
KK -> O
CN -> H
FP -> K
VH -> K
VK -> P
HP -> S
FK -> F
BK -> H
KV -> V
BB -> O
KC -> F
KN -> C
PO -> P
NF -> P
PN -> S
PF -> S
PK -> O"""

tdata = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def part2(data: str, debug: bool = False):

    def ans(p):
        from collections import Counter
        c = Counter(p)
        print(c.most_common()[0])
        print(c.most_common()[-1])
        print(c.most_common()[0][1] - c.most_common()[-1][1])

    steps = 40
    blocks = data.split('\n\n')
    poly = blocks[0]
    conv = {}
    for line in blocks[1].splitlines():
        words = line.split(' -> ')
        conv[words[0]] = words[1]

    for step in range(steps):
        print('Step', step)
        ans(poly)

        new_poly = []
        for i in range(0, len(poly) - 1):
            pair = ''.join(poly[i:i + 2])
            new_poly.append(poly[i])
            if pair in conv:
                new_poly.append(conv[pair])
        new_poly.append(poly[-1])
        poly = new_poly

    ans(poly)


def part1(data: str, debug: bool = False):
    steps = 10
    blocks = data.split('\n\n')
    poly = blocks[0]
    conv = {}
    for line in blocks[1].splitlines():
        words = line.split(' -> ')
        conv[words[0]] = words[1]

    if debug:
        print('Polymer', poly)
        print(conv)

    for _ in range(steps):
        if debug:
            print(poly)
        new_poly = []
        for i in range(0, len(poly) - 1):
            pair = ''.join(poly[i:i + 2])
            new_poly.append(poly[i])
            if pair in conv:
                new_poly.append(conv[pair])
        new_poly.append(poly[-1])
        poly = new_poly

    if debug:
        print(poly)

    from collections import Counter
    c = Counter(poly)
    print(c)
    print(c.most_common()[0])
    print(c.most_common()[-1])
    print(c.most_common()[0][1] - c.most_common()[-1][1])


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
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
