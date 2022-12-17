from utils.measure import checker


def solution1(A):
    s = set()
    for a in A:
        if a-1 in s or a + 1 in s:
            return True
        s.add(a)
    return False


def solution2(A):
    if len(A) < 2:
        return False
    A.sort()
    for i in range(1, len(A)):
        if A[i] == A[i - 1] + 1:
            return True

    return False


if __name__ == '__main__':
    import numpy as np
    busy = list(np.random.randint(1, 2_000_000, size=1_000_000))
    sparse = list(np.random.randint(1, 2_000_000, size=1000))

    with checker(solution1, repeat=100) as c:
        c.check_1([11, 1, 8, 124, 1], False)
        c.check_1([7], False)
        c.check_1([4, 3], True)
        c.check_1([5, 5, 5, 5,], False)
        c.check_1(busy, True)
        c.check_1(sparse, False)

    with checker(solution2, repeat=100) as c:
        c.check_1([11, 1, 8, 124, 1], False)
        c.check_1([7], False)
        c.check_1([4, 3], True)
        c.check_1([5, 5, 5, 5, ], False)
        c.check_1(busy, True)
        c.check_1(sparse, False)

