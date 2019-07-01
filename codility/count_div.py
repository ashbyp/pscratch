# Write a function:
#
# def solution(A, B, K)
#
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that
# are divisible by K, i.e.:
#
# { i : A ≤ i ≤ B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers
# divisible by 2 within the range [6..11], namely 6, 8 and 10.
#
# Write an efficient algorithm for the following assumptions:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.


def solution_order_B_minus_A(A, B, K):
    C = 0
    for i in range(A, B+1):
        if i % K == 0:
            C += 1
    return C


def solution_order_B_minus_A_divided_by_K(A, B, K):
    C = 0
    for i in range(A, B+1):
        if i % K == 0:
            C += 1
            for j in range(i+K, B+1, K):
                C += 1
            break
    return C


def solution(A, B, K):
    return solution_order_B_minus_A_divided_by_K(A, B, K)


if __name__ == '__main__':
    print(solution(6, 11, 2))