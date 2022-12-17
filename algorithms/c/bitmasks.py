def zeros(n):
    res = 0
    for i in range(30):
        if n % 2 == 0:
            res += 1
        n >>= 1
    return res


def confs(n):
    return 1 << zeros(n)


def solution(A, B, C):
    common = confs(A | B) + confs(A | C) + confs(B | C) - confs(A | B | C)
    return confs(A) + confs(B) + confs(C) - common


if __name__ == '__main__':
    A = 1_073_741_727
    B = 1_073_741_631
    C = 1_073_741_679

    print(solution(A, B, C))
