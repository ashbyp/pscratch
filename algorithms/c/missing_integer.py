# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that
# does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    # write your code in Python 2.7
    A.sort()
    M = 1
    for v in A:
        if v == M:
            M += 1
    return M


if __name__ == '__main__':
    import random
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))
    print(solution([]))
    print(solution([1]))
    print(solution([2]))
    print(solution([-2]))
    x = list(range(0, 100))
    random.shuffle(x)
    print(solution(list(x)))