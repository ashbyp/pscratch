def solution(A):
    l = 1
    x = A[0]
    while x != -1:
        x = A[x]
        l += 1
    return l


if __name__ == '__main__':
    print(solution([1, 4, -1, 3, 2]))
