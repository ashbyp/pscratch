question = "https://adventofcode.com/2024/day/24"
input_data = "https://adventofcode.com/2024/day/24/input"

pdata = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
x05: 0
x06: 1
x07: 1
x08: 0
x09: 1
x10: 1
x11: 1
x12: 1
x13: 0
x14: 0
x15: 1
x16: 0
x17: 0
x18: 1
x19: 1
x20: 0
x21: 1
x22: 1
x23: 0
x24: 1
x25: 0
x26: 1
x27: 1
x28: 1
x29: 1
x30: 0
x31: 0
x32: 0
x33: 0
x34: 0
x35: 0
x36: 0
x37: 1
x38: 0
x39: 0
x40: 0
x41: 0
x42: 0
x43: 1
x44: 1
y00: 1
y01: 0
y02: 0
y03: 1
y04: 1
y05: 0
y06: 0
y07: 0
y08: 0
y09: 0
y10: 0
y11: 1
y12: 0
y13: 1
y14: 1
y15: 0
y16: 1
y17: 0
y18: 1
y19: 0
y20: 0
y21: 0
y22: 1
y23: 1
y24: 0
y25: 0
y26: 1
y27: 0
y28: 0
y29: 1
y30: 0
y31: 1
y32: 1
y33: 1
y34: 0
y35: 0
y36: 0
y37: 0
y38: 1
y39: 1
y40: 0
y41: 0
y42: 0
y43: 1
y44: 1

x14 AND y14 -> cwj
dhf OR hrr -> gcs
y44 XOR x44 -> pfh
fqq OR hww -> bpg
wmd OR kvv -> jts
khg AND hdd -> nfn
y35 XOR x35 -> rpk
bhw XOR sth -> htp
x13 XOR y13 -> gnf
y39 AND x39 -> qwn
nhr XOR wks -> z19
x40 AND y40 -> mpd
pvw AND fsf -> hsf
y29 AND x29 -> sbk
kqk OR shk -> gjs
swm OR rrk -> fww
x30 AND y30 -> bpn
mts XOR ntr -> z02
y23 XOR x23 -> vsh
x07 XOR y07 -> cwh
jqq OR trc -> wrr
y14 XOR x14 -> khg
y12 XOR x12 -> fsf
x27 AND y27 -> tts
bjs AND vnp -> tsp
hcq OR pjv -> fvm
vsk XOR svf -> z42
dwp AND fwn -> rsm
x30 XOR y30 -> bjs
y19 AND x19 -> pjv
x20 XOR y20 -> mvv
vpb XOR jmq -> z43
tkd AND shd -> thc
nbw XOR wjn -> z38
wjn AND nbw -> jqq
y17 XOR x17 -> hhm
dkr OR fdd -> bvc
qjh AND qcm -> mcd
x26 XOR y26 -> fwn
dsf AND tjv -> bsh
qjs AND ncw -> nhw
nsg XOR kkt -> z04
hhb OR htp -> mqr
hgs XOR hhh -> z21
wrr XOR htw -> z39
cwh XOR tpd -> z07
gcs XOR hdc -> dkr
rng AND mdw -> rhp
cwh AND tpd -> ddj
x43 AND y43 -> jjk
hhm AND jts -> swm
x04 AND y04 -> hrr
qhg OR jgj -> shd
y44 AND x44 -> kbb
gpb AND cwn -> prp
y42 AND x42 -> vcd
y38 AND x38 -> trc
mvv XOR fvm -> hhh
qjh XOR qcm -> z33
y05 AND x05 -> z05
pfh AND gqg -> khw
y03 XOR x03 -> tkd
x25 XOR y25 -> dwk
phm AND bjw -> bcm
y31 XOR x31 -> gpb
y28 AND x28 -> pcd
hdc AND gcs -> fdd
ffw XOR cjf -> z11
y21 XOR x21 -> hgs
fcd XOR nkw -> z41
kqs XOR vjk -> z22
x36 AND y36 -> ggk
x34 XOR y34 -> tjv
y25 AND x25 -> cbg
x24 XOR y24 -> mdw
rpk AND rfs -> fkk
x24 AND y24 -> rwd
y11 AND x11 -> mdb
phm XOR bjw -> z40
tsp OR bpn -> cwn
y29 XOR x29 -> nrv
nhw OR qdc -> qcm
tjv XOR dsf -> z34
x21 AND y21 -> mvp
x08 AND y08 -> bnr
gqr OR mdb -> pvw
sfw AND gnf -> tsh
mfc AND gqf -> bwd
y35 AND x35 -> nbb
x09 XOR y09 -> csk
qfj OR mqg -> z20
x22 AND y22 -> kqk
x08 XOR y08 -> wcg
y37 XOR x37 -> mfc
wrn XOR fww -> z18
rvw OR rsm -> dnb
x23 AND y23 -> mcw
wwc OR hch -> ntr
x22 XOR y22 -> vjk
gqf XOR mfc -> z37
sth AND bhw -> z15
rng XOR mdw -> z24
y04 XOR x04 -> kkt
fsf XOR pvw -> z12
bpg XOR kpk -> z10
x02 AND y02 -> qhg
x19 XOR y19 -> nhr
cbg OR srg -> dwp
pfh XOR gqg -> z44
y00 AND x00 -> wsg
x33 XOR y33 -> qjh
jts XOR hhm -> z17
y32 XOR x32 -> ncw
fww AND wrn -> gfq
qcn OR fjq -> vsk
nsg AND kkt -> dhf
y32 AND x32 -> qdc
bgf OR sfb -> tpd
dnb AND bsv -> bcn
y28 XOR x28 -> phk
tds AND mqr -> kvv
wtf OR qwn -> phm
pss XOR csk -> z09
kwp OR sbk -> vnp
y26 AND x26 -> rvw
mvv AND fvm -> qfj
y15 AND x15 -> hhb
hbb XOR nrv -> z29
dsn AND wcg -> rms
bnr OR rms -> pss
nfn OR cwj -> sth
mvp OR wms -> kqs
khg XOR hdd -> z14
bwd OR rnr -> wjn
x18 AND y18 -> twv
rfs XOR rpk -> z35
dwk AND fbs -> srg
prp OR dmf -> qjs
nbb OR fkk -> hpg
ncw XOR qjs -> z32
pcd OR wff -> hbb
y43 XOR x43 -> jmq
hkg OR mcw -> rng
x09 AND y09 -> hww
y13 AND x13 -> fhs
qfg AND bvc -> bgf
y18 XOR x18 -> wrn
phk XOR rkf -> z28
x06 XOR y06 -> qfg
y00 XOR x00 -> z00
x16 XOR y16 -> tds
hgs AND hhh -> wms
fkc OR vcd -> vpb
y03 AND x03 -> rrr
thc OR rrr -> nsg
sfw XOR gnf -> z13
bvc XOR qfg -> z06
wsg AND pnw -> hch
y39 XOR x39 -> htw
x12 AND y12 -> npc
vjk AND kqs -> shk
ggk XOR hpg -> z36
gjs XOR vsh -> z23
ddj OR ktn -> dsn
x38 XOR y38 -> nbw
y33 AND x33 -> mqv
ggk AND hpg -> bqf
npc OR hsf -> sfw
y16 AND x16 -> wmd
vsh AND gjs -> hkg
x10 XOR y10 -> kpk
mcd OR mqv -> dsf
x05 XOR y05 -> hdc
wcg XOR dsn -> z08
x41 XOR y41 -> nkw
mts AND ntr -> jgj
bcm OR mpd -> fcd
tds XOR mqr -> z16
vsk AND svf -> fkc
x27 XOR y27 -> bsv
bqf OR rhv -> gqf
kbb OR khw -> z45
nrv AND hbb -> kwp
csk AND pss -> fqq
y34 AND x34 -> cjq
x20 AND y20 -> mqg
tsh OR fhs -> hdd
wks AND nhr -> hcq
cjq OR bsh -> rfs
gfq OR twv -> wks
rwd OR rhp -> fbs
y37 AND x37 -> rnr
vfs OR jgd -> cjf
y31 AND x31 -> dmf
kpk AND bpg -> jgd
y36 XOR x36 -> rhv
y42 XOR x42 -> svf
bjs XOR vnp -> z30
cst OR jjk -> gqg
y40 XOR x40 -> bjw
cjf AND ffw -> gqr
fcd AND nkw -> fjq
y01 XOR x01 -> pnw
dnb XOR bsv -> z27
wsg XOR pnw -> z01
y41 AND x41 -> qcn
y06 AND x06 -> sfb
gpb XOR cwn -> z31
x02 XOR y02 -> mts
shd XOR tkd -> z03
dwk XOR fbs -> z25
y11 XOR x11 -> ffw
phk AND rkf -> wff
jmq AND vpb -> cst
bcn OR tts -> rkf
y07 AND x07 -> ktn
x17 AND y17 -> rrk
x10 AND y10 -> vfs
fwn XOR dwp -> z26
x01 AND y01 -> wwc
htw AND wrr -> wtf
y15 XOR x15 -> bhw"""

# pdata="""x00: 0
# x01: 1
# x02: 0
# x03: 1
# x04: 0
# x05: 1
# y00: 0
# y01: 0
# y02: 1
# y03: 1
# y04: 0
# y05: 1
#
# x00 AND y00 -> z00
# x01 AND y01 -> z01
# x02 AND y02 -> z02
# x03 AND y03 -> z03
# x04 AND y04 -> z04
# x05 AND y05 -> z05"""

tdata = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


class Gate:
    OP = None

    def __init__(self, in1, in2, out):
        self.input_1 = in1
        self.input_2 = in2
        self.output = out
        self.input_signal_1 = None
        self.input_signal_2 = None

    def is_active(self):
        return self.input_signal_1 is not None and self.input_signal_2 is not None

    def set(self, node, sig):
        if node == self.input_1:
            self.input_signal_1 = sig
        if node == self.input_2:
            self.input_signal_2 = sig

    def __str__(self):
        return f'{self.input_1} {self.OP} {self.input_2} -> {self.output} active = {self.input_signal_1} {self.input_signal_2}, sig= {self.signal()}'

    def __repr__(self):
        return self.__str__()


class And(Gate):
    OP = 'and'

    def __init__(self, in1, in2, out):
        super().__init__(in1, in2, out)

    def signal(self):
        if self.is_active():
            return self.input_signal_1 & self.input_signal_2


class Or(Gate):
    OP = 'or'

    def __init__(self, in1, in2, out):
        super().__init__(in1, in2, out)

    def signal(self):
        if self.is_active():
            return self.input_signal_1 | self.input_signal_2


class Xor(Gate):
    OP = 'xor'

    def __init__(self, in1, in2, out):
        super().__init__(in1, in2, out)

    def signal(self):
        if self.is_active():
            return self.input_signal_1 ^ self.input_signal_2


def create(gate1, op, gate2, gate3):
    if op == 'AND':
        return And(gate1, gate2, gate3)
    elif op == 'OR':
        return Or(gate1, gate2, gate3)
    elif op == 'XOR':
        return Xor(gate1, gate2, gate3)
    else:
        raise


def send(network, node, signal, endpoints):
    for connected_node in network[node]:
        connected_node.set(node, signal)

        if connected_node.is_active():
            if connected_node.output.startswith('z'):
                endpoints.append((connected_node.output, connected_node.signal()))
            else:
                send(network, connected_node.output, connected_node.signal(), endpoints)


def part2(data: str, _debug: bool = False):
    blocks = data.split('\n\n')
    from collections import defaultdict

    network = defaultdict(list)
    for node in blocks[1].splitlines():
        input_1, op, input_2, _, output = node.split()
        node = create(input_1, op, input_2, output)
        network[input_1].append(node)
        network[input_2].append(node)

    if _debug:
        from pprint import pprint
        pprint(network)

    x_inputs = []
    y_inputs = []
    outputs = []

    for input in blocks[0].splitlines():
        node, signal = input.split(':')
        signal = int(signal)
        if node.startswith('x'): x_inputs.append((node, signal))
        if node.startswith('y'): y_inputs.append((node, signal))
        send(network, node, signal, outputs)

    if _debug:
        pprint(network)
        pprint(sorted(outputs, reverse=True))

    b = ''.join([str(x[1]) for x in sorted(outputs, reverse=True)])
    print(b)
    ANS = int(b, 2)

    b = ''.join([str(x[1]) for x in sorted(x_inputs, reverse=True)])
    print(' ' + b)
    ARG1 = int(b, 2)

    b = ''.join([str(x[1]) for x in sorted(y_inputs, reverse=True)])
    print(' ' + b)
    ARG2 = int(b, 2)

    print(f'ANS={ANS} ARG1={ARG1} ARG2={ARG2}  ERROR={ANS - ARG1 - ARG2}')


def part1(data: str, _debug: bool = False):
    blocks = data.split('\n\n')
    from collections import defaultdict

    network = defaultdict(list)
    for node in blocks[1].splitlines():
        input_1, op, input_2, _, output = node.split()
        node = create(input_1, op, input_2, output)
        network[input_1].append(node)
        network[input_2].append(node)

    if _debug:
        from pprint import pprint
        pprint(network)

    outputs = []

    for input in blocks[0].splitlines():
        node, signal = input.split(':')
        signal = int(signal)
        send(network, node, signal, outputs)

    if _debug:
        pprint(network)
        pprint(sorted(outputs, reverse=True))

    b = ''.join([str(x[1]) for x in sorted(outputs, reverse=True)])
    print(b)
    print(int(b, 2))


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
