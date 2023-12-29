pdata = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0"""
tdata = """"""

data = pdata


def run(nums):
    pc = 0
    while nums[pc] != 99:
        op = nums[pc]
        a = nums[pc + 1]
        b = nums[pc + 2]
        c = nums[pc + 3]

        if op == 1:
            nums[c] = nums[a] + nums[b]
        else:
            nums[c] = nums[a] * nums[b]
        pc += 4

    return nums[0]


def part2():
    target = 19690720
    for noun in range(100):
        for verb in range(100):
            nums = list(map(int, data.split(',')))
            nums[1] = noun
            nums[2] = verb
            state = run(nums)
            if state == target:
                print(100 * noun + verb)
                return


def part1():
    nums = list(map(int, data.split(',')))
    nums[1] = 12
    nums[2] = 2
    print(run(nums))


if __name__ == '__main__':
    part1()
    part2()
