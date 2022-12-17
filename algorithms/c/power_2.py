

def solution(N):
    if N % 2 != 0:
        return 0

    p = 1
    a = 1

    while True:
        x = 2**p
        if x > N:
            break
        if (N % x) == 0:
            a = p
        p += 1

    return a


if __name__ == '__main__':
    # print(solution(1))
    # print(solution(24))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))