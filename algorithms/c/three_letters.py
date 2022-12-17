
def solution(A, B):
    # write your code in Python 3.6
    res = ""

    while A or B:
        if res[-2:] == "aa":
            res += "b"
            B -= 1
        elif res[-2:] == "bb":
            res += "a"
            A -= 1
        elif A > B:
            res += "a"
            A -= 1
        else:
            res += "b"
            B -= 1

    return res


if __name__ == '__main__':
    print(solution(5, 3))
    print(solution(3, 3))
    print(solution(1, 4))