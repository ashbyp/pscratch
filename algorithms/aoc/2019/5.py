data = """3,225,1,225,6,6,1100,1,238,225,104,0,1101,61,45,225,102,94,66,224,101,-3854,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,31,30,225,1102,39,44,224,1001,224,-1716,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,92,41,225,101,90,40,224,1001,224,-120,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,51,78,224,101,-129,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1,170,13,224,101,-140,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,14,58,225,1102,58,29,225,1102,68,70,225,1002,217,87,224,101,-783,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,19,79,225,1001,135,42,224,1001,224,-56,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,2,139,144,224,1001,224,-4060,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,9,51,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,102,2,223,223,1006,224,329,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,464,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,494,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,614,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,644,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"""

# data = """3,0,4,0,99"""
# data = """1002,4,3,4,33"""
# data = """3,9,8,9,10,9,4,9,99,-1,8"""
POS = 0
IMM = 1


def part2():
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
            i = int(input("Enter a number: "))
            nums[a] = i
            pc += 2

        elif op == 4:
            a = nums[pc + 1]
            print(nums[a] if a_m == POS else a)
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


def part1():
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
            i = int(input("Enter a number: "))
            nums[a] = i
            pc += 2

        elif op == 4:
            a = nums[pc + 1]
            print(nums[a] if a_m == POS else a)
            pc += 2

        else:
            raise ValueError('Invalid opcode:' + str(op))


if __name__ == '__main__':
    # part1()
    part2()
