pdata = """"""

tdata = """"""


def part2(data):
    pass


def part1(data):
    pass


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
