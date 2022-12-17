from utils.measure import checker


def solution1(S):
    i = int(S, 2)
    ops = 0

    while i:
        if i % 2 == 0:
            i = i // 2
        else:
            i -= 1
        ops += 1

    return ops


def solution2(S):
    S = list(S.lstrip('0'))
    p = len(S) - 1
    c = 0

    while p >= 0:
        if S[p] == '0':
            p -= 1
            if p:
                c += 1
        else:
            S[p] = '0'
            c += 1

    return c


def solution3(S):
    S = S.lstrip('0')
    p = len(S) - 1
    c = 0
    last_one = False

    while p >= 0:
        if last_one or S[p] == '0':
            last_one = False
            p -= 1
            if p:
                c += 1
        else:
            c += 1
            last_one = True

    return c


def solution4(S):
    S = S.lstrip('0')
    c = 0
    for i in range(len(S) -1, -1, -1):
        if S[i] == '1':
            if i:
                c += 2
            else:
                c += 1
        else:
            c += 1
    return c


def solution5(S):
    S = S.lstrip('0')
    l = len(S)
    ones = sum(1 if x == '1' else 0 for x in S)
    zeros = l - ones
    return ones * 2 - 1 + zeros


def solution6(S):
    p = 0
    ones = 0
    zeros = 0
    l = len(S)
    while p < l:
        if S[p] == '1':
            ones += 1
        elif ones:
            zeros += 1
        p += 1
    return ones * 2 - 1 + zeros


if __name__ == '__main__':
    big = '1' * 50000
    bigger = '1' * 400000

    with checker(solution1, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        #c.check_1(bigger, 799999)

    with checker(solution2, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        c.check_1(bigger, 799999)

    with checker(solution3, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        c.check_1(bigger, 799999)

    with checker(solution4, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        c.check_1(bigger, 799999)

    with checker(solution5, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        c.check_1(bigger, 799999)

    with checker(solution6, repeat=0) as c:
        c.check_1('10', 2)
        c.check_1('011100', 7)
        c.check_1('111', 5)
        c.check_1(big, 99999)
        c.check_1(bigger, 799999)











