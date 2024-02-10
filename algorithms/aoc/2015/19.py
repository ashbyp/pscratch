pdata = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"""

tdata = """H => HO
H => OH
O => HH

HOH"""

tdata2="""e => H
e => O
H => HO
H => OH
O => HH

HOH"""


def part2(data: str, debug: bool = False):
    blocks = data.split('\n\n')
    trans = []
    for ins in blocks[0].splitlines():
        words = ins.split(' ')
        trans.append((words[2], words[0]))
    molecule = blocks[1]

    trans = sorted(trans, key=lambda x: len(x[0]), reverse=True)

    if debug:
        print(trans)
        print(molecule)

    steps = 0

    while molecule != 'e':
        for t in trans:
            if t[0] in molecule:
                break
        while t[0] in molecule:
            molecule = molecule.replace(t[0], t[1])
            steps += 1
        if debug:
            print(molecule)

    print('Steps:', steps)




def part1(data: str, debug: bool = False):
    blocks = data.split('\n\n')
    from collections import defaultdict
    trans = defaultdict(list)
    for ins in blocks[0].splitlines():
        words = ins.split(' ')
        trans[words[0]].append(words[2])

    if debug:
        print(trans)
    molecule = blocks[1]
    if debug:
        print('_', molecule, '_')

    modules = set()
    for i in range(len(molecule)):
        for k, v in trans.items():
            if debug:
                print(' Try', k, 'on', molecule[i:])
            if molecule[i:].startswith(k):
                bef = molecule[:i]
                aft = molecule[i + len(k):]
                for replacement in v:
                    if debug:
                        print(' add ', bef, replacement, aft)
                    modules.add(bef + replacement + aft)
    if debug:
        print(modules)
    print(len(modules))


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

    # run("Part 1 test", tdata, part1, True)
    # run("Part 1 puzzle", pdata, part1, False)
    # run("Part 2 test", tdata2, part2, True)
    run("Part 2 puzzle", pdata, part2, False)


if __name__ == '__main__':
    main()
