data = """3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,5,9,9,1001,9,2,9,102,2,9,9,101,3,9,9,1002,9,2,9,4,9,99,3,9,101,5,9,9,102,5,9,9,1001,9,2,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,5,9,1001,9,5,9,1002,9,4,9,101,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99"""
# data = """3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"""

POS = 0
IMM = 1


def run(phases: list[int]):
    last_output = 0

    for run_num in range(len(phases)):
        provided_phase = False
        nums = list(map(int, data.split(',')))
        pc = 0
        while nums[pc] != 99:
            op = nums[pc]
            a_m, b_m, c_m = POS, POS, POS
            if op > 9:
                sop = str(op)
                op = int(sop[-2:])
                if len(sop) > 2:
                    a_m = int(sop[-3])
                if len(sop) > 3:
                    b_m = int(sop[-4])
                if len(sop) > 4:
                    c_m = int(sop[-5])

            if op == 1:
                a = nums[pc + 1]
                b = nums[pc + 2]
                c = nums[pc + 3]
                nums[c] = (nums[a] if a_m == POS else a) + (nums[b] if b_m == POS else b)
                pc += 4

            elif op == 2:
                a = nums[pc + 1]
                b = nums[pc + 2]
                c = nums[pc + 3]
                nums[c] = (nums[a] if a_m == POS else a) * (nums[b] if b_m == POS else b)
                pc += 4

            elif op == 3:
                a = nums[pc + 1]
                if not provided_phase:
                    i = phases[run_num]
                    provided_phase = True
                else:
                    i = last_output

                nums[a] = i
                pc += 2

            elif op == 4:
                a = nums[pc + 1]
                last_output = nums[a] if a_m == POS else a
                pc += 2

            elif op == 5:
                """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the 
                instruction pointer to the value from the second parameter. 
                Otherwise, it does nothing"""
                a = nums[pc + 1]
                b = nums[pc + 2]

                if (nums[a] if a_m == POS else a) != 0:
                    pc = (nums[b] if b_m == POS else b)
                else:
                    pc += 3

            elif op == 6:
                """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the 
                instruction pointer to the value from the second parameter. 
                Otherwise, it does nothing"""
                a = nums[pc + 1]
                b = nums[pc + 2]

                if (nums[a] if a_m == POS else a) == 0:
                    pc = (nums[b] if b_m == POS else b)
                else:
                    pc += 3


            elif op == 7:
                """Opcode 7 is less than: if the first parameter is less than the second 
                parameter, it stores 1 in the position given by the third parameter. 
                Otherwise, it stores 0"""
                a = nums[pc + 1]
                b = nums[pc + 2]
                c = nums[pc + 3]

                if (nums[a] if a_m == POS else a) < (nums[b] if b_m == POS else b):
                    nums[c] = 1
                else:
                    nums[c] = 0
                pc += 4

            elif op == 8:
                """Opcode 8 is equals: if the first parameter is 
                equal to the second parameter, it stores 1 in the position given 
                by the third parameter. Otherwise, it stores 0."""
                a = nums[pc + 1]
                b = nums[pc + 2]
                c = nums[pc + 3]

                if (nums[a] if a_m == POS else a) == (nums[b] if b_m == POS else b):
                    nums[c] = 1
                else:
                    nums[c] = 0
                pc += 4

            else:
                raise ValueError('Invalid opcode:' + str(op))

    return last_output

def run2(phases: list[int]):
    last_output = 0
    machines = [[list(map(int, data.split(','))), 0, p] for p in phases]

    # print(machines)

    run_num = -1
    while True:
        run_num += 1
        machine = machines[run_num % len(machines)]
        while True:
            if machine[0][machine[1]] == 99:
                # print(last_output)
                return last_output
            op = machine[0][machine[1]]
            a_m, b_m, c_m = POS, POS, POS
            if op > 9:
                sop = str(op)
                op = int(sop[-2:])
                if len(sop) > 2:
                    a_m = int(sop[-3])
                if len(sop) > 3:
                    b_m = int(sop[-4])
                if len(sop) > 4:
                    c_m = int(sop[-5])

            if op == 1:
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]
                c = machine[0][machine[1] + 3]
                machine[0][c] = (machine[0][a] if a_m == POS else a) + (machine[0][b] if b_m == POS else b)
                machine[1] += 4

            elif op == 2:
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]
                c = machine[0][machine[1] + 3]
                machine[0][c] = (machine[0][a] if a_m == POS else a) * (machine[0][b] if b_m == POS else b)
                machine[1] += 4

            elif op == 3:
                a = machine[0][machine[1] + 1]
                if machine[2] != -1:
                    i = machine[2]
                    machine[2] = -1
                else:
                    i = last_output

                # print('providing', i)

                machine[0][a] = i
                machine[1] += 2

            elif op == 4:
                a = machine[0][machine[1] + 1]
                last_output = machine[0][a] if a_m == POS else a
                machine[1] += 2

                # print('output was', last_output)

                break

            elif op == 5:
                """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the 
                instruction pointer to the value from the second parameter. 
                Otherwise, it does nothing"""
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]

                if (machine[0][a] if a_m == POS else a) != 0:
                    machine[1] = (machine[0][b] if b_m == POS else b)
                else:
                    machine[1] += 3

            elif op == 6:
                """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the 
                instruction pointer to the value from the second parameter. 
                Otherwise, it does nothing"""
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]

                if (machine[0][a] if a_m == POS else a) == 0:
                    machine[1] = (machine[0][b] if b_m == POS else b)
                else:
                    machine[1] += 3


            elif op == 7:
                """Opcode 7 is less than: if the first parameter is less than the second 
                parameter, it stores 1 in the position given by the third parameter. 
                Otherwise, it stores 0"""
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]
                c = machine[0][machine[1] + 3]

                if (machine[0][a] if a_m == POS else a) < (machine[0][b] if b_m == POS else b):
                    machine[0][c] = 1
                else:
                    machine[0][c] = 0
                machine[1] += 4

            elif op == 8:
                """Opcode 8 is equals: if the first parameter is 
                equal to the second parameter, it stores 1 in the position given 
                by the third parameter. Otherwise, it stores 0."""
                a = machine[0][machine[1] + 1]
                b = machine[0][machine[1] + 2]
                c = machine[0][machine[1] + 3]

                if (machine[0][a] if a_m == POS else a) == (machine[0][b] if b_m == POS else b):
                    machine[0][c] = 1
                else:
                    machine[0][c] = 0
                machine[1] += 4

            else:
                raise ValueError('Invalid opcode:' + str(op))

def part2():
    print('part 2')
    max_output = 0
    from itertools import permutations
    for permutation in permutations(range(5, 10)):
        max_output = max(max_output, run2(permutation))
    print(max_output)


def part1():
    print('part 1')
    max_output = 0
    from itertools import permutations
    for permutation in permutations(range(5)):
        max_output = max(max_output, run(permutation))
    print(max_output)


if __name__ == '__main__':
    part1()
    part2()
