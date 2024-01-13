pdata = """"""

tdata = """"""


def part2(data: str, debug: bool = False):
    pass


def part1(data: str, debug: bool = False):
    pass


if __name__ == '__main__':
    def run(msg, data, fn, debug):
        if data:
            print(f'{msg:15} ------------')
            fn(data, debug)
            print()


    run("Part 1 test", tdata, part1, True)
    run("Part 1 puzzle", pdata, part1, False)
    run("Part 2 test", tdata, part2, True)
    run("Part 2 puzzle", pdata, part2, False)
