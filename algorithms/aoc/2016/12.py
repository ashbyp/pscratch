pdata = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

tdata = """"""


def part2(data: str, debug: bool = False):
    ins = data.splitlines()
    reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    pc = 0

    while pc < len(ins):
        i = ins[pc].split()
        match i[0]:
            case 'cpy':
                if i[1].isdigit():
                    reg[i[2]] = int(i[1])
                else:
                    reg[i[2]] = reg[i[1]]
                pc += 1
            case 'inc':
                reg[i[1]] = reg[i[1]] + 1
                pc += 1
            case 'dec':
                reg[i[1]] = reg[i[1]] - 1
                pc += 1
            case 'jnz':
                if i[1].isdigit():
                    x = int(i[1])
                else:
                    x = reg[i[1]]
                if x:
                    pc += int(i[2])
                else:
                    pc += 1
            case _:
                raise ValueError(i)

    print(reg['a'])


def part1(data: str, debug: bool = False):
    ins = data.splitlines()
    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    pc = 0

    while pc < len(ins):
        i = ins[pc].split()
        match i[0]:
            case 'cpy':
                if i[1].isdigit():
                    reg[i[2]] = int(i[1])
                else:
                    reg[i[2]] = reg[i[1]]
                pc += 1
            case 'inc':
                reg[i[1]] = reg[i[1]] + 1
                pc += 1
            case 'dec':
                reg[i[1]] = reg[i[1]] - 1
                pc += 1
            case 'jnz':
                if i[1].isdigit():
                    x = int(i[1])
                else:
                    x = reg[i[1]]
                if x:
                    pc += int(i[2])
                else:
                    pc +=1
            case _:
                raise ValueError(i)

    print(reg['a'])

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
