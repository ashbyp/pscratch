pdata = """1113122113"""

tdata = """"""


def part2(data: str, debug: bool = False):
    nums = list(map(int, data))
    for i in range(50):
        next_data = []
        last, count = nums[0], 1
        for n in nums[1:]:
            if n == last:
                count += 1
            else:
                next_data.append(count)
                next_data.append(last)
                last = n
                count = 1
        next_data.append(count)
        next_data.append(last)
        nums = next_data
        print(i)
    print(len(nums))


def part1(data: str, debug: bool = False):
    nums = list(map(int, data))
    for i in range(40):
        next_data = []
        last, count = nums[0], 1
        for n in nums[1:]:
            if n == last:
                count += 1
            else:
                next_data.append(count)
                next_data.append(last)
                last = n
                count = 1
        next_data.append(count)
        next_data.append(last)
        nums = next_data
        print(i)
    print(len(nums))


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
