from utils.measure import checker


def solution(A):
    min_cost = None
    for i, cost in enumerate(A[1:], start=1):
        base_cost = A[i]
        if not min_cost or (min_cost > base_cost):
            for j in range(i+2, len(A) - 1):
                break_cost = base_cost + A[j]
                if not min_cost or break_cost < min_cost:
                    min_cost = break_cost

    return min_cost

# Example usage:
A = [5, 2, 4, 6, 3, 7]
print(solution(A))

with checker(solution, repeat=0, check_success=True) as c:
    c.check_1([5, 2, 4, 6, 3, 7] + [1000] * 1000, 5)

