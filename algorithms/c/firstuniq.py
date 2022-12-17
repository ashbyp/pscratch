# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from utils.measure import timefunc


@timefunc('zero', 2_000_000)
def solution(A):
    tally = dict.fromkeys(A, 0)
    for a in A:
        tally[a] += 1
    for a in A:
        if tally[a] == 1:
            return a
    return -1


@timefunc('one', 2_000_000)
def solution1(A):
    from collections import Counter
    c = Counter(A)
    for a in A:
        if c[a] == 1:
            return a
    return -1


@timefunc('two', 2_000_000)
def solution2(A):
    tally = {}
    for a in A:
        if a not in tally:
            tally[a] = 1
        else:
            tally[a] += 1
    for a in A:
        if tally[a] == 1:
            return a
    return -1


@timefunc('three', 2_000_000)
def solution3(A):
    tally = {}
    for a in A:
        tally[a] = tally.get(a, 0) + 1
        #
        # if a not in tally:
        #     tally[a] = 1
        # else:
        #     tally[a] += 1
    for a in A:
        if tally[a] == 1:
            return a
    return -1


if __name__ == '__main__':
    print(solution([4, 10, 5, 4, 2, 10]))
    print(solution([6, 4, 4, 6]))
    print('----')
    print(solution1([4, 10, 5, 4, 2, 10]))
    print(solution1([6, 4, 4, 6]))
    print('----')
    print(solution2([4, 10, 5, 4, 2, 10]))
    print(solution2([6, 4, 4, 6]))
    print('----')
    print(solution3([4, 10, 5, 4, 2, 10]))
    print(solution3([6, 4, 4, 6]))