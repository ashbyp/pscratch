pdata = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

tdata = """"""


def part2(data: str, debug: bool = False):
    ins = data.splitlines()
    n_ins = len(ins)
    pc = 0
    reg = {'a': 1, 'b': 0}

    while pc < n_ins:
        i = ins[pc].replace(',', '').split()
        cur = i[0]
        match cur:
            case 'hlf':
                reg[i[1]] = reg[i[1]] / 2
                pc += 1
            case 'tpl':
                reg[i[1]] = reg[i[1]] * 3
                pc += 1
            case 'inc':
                reg[i[1]] = reg[i[1]] + 1
                pc += 1
            case 'jmp':
                pc = pc + int(i[1])
            case 'jie':
                if (reg[i[1]] % 2) == 0:
                    pc = pc + int(i[2])
                else:
                    pc += 1
            case 'jio':
                if reg[i[1]] == 1:
                    pc = pc + int(i[2])
                else:
                    pc += 1
            case _:
                raise ValueError(i[0])

    print('b=', reg['b'])


def part1(data: str, debug: bool = False):
    ins = data.splitlines()
    n_ins = len(ins)
    pc = 0
    reg = { 'a': 0, 'b': 0}

    while pc < n_ins:
        i = ins[pc].replace(',', '').split()
        cur = i[0]
        match cur:
            case 'hlf':
                reg[i[1]] = reg[i[1]] / 2
                pc += 1
            case 'tpl':
                reg[i[1]] = reg[i[1]] * 3
                pc += 1
            case'inc':
                reg[i[1]] = reg[i[1]] + 1
                pc += 1
            case 'jmp':
                pc = pc + int(i[1])
            case 'jie':
                if (reg[i[1]] % 2) == 0:
                    pc = pc + int(i[2])
                else:
                    pc += 1
            case 'jio':
                if reg[i[1]] == 1:
                    pc = pc + int(i[2])
                else:
                    pc += 1
            case _:
                raise ValueError(i[0])

    print('b=', reg['b'])

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
