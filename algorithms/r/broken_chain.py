from utils.measure import checker
import math

def solution(A):
    min_cost = float('inf')
    for i, cost in enumerate(A[1:], start=1):
        base_cost = cost
        if min_cost > base_cost:
            for j in range(i+2, len(A) - 1):
                break_cost = base_cost + A[j]
                min_cost = min(min_cost, break_cost)
    return min_cost



def minSum(array):
    _min = array[1]
    result = math.inf

    print(array)

    for i in range(3, len(array) - 1):
        print('--------')
        print('i=', i)
        print('array[i-2]', array[i-2])
        _min = min(_min, array[i-2])
        print('_min', _min)
        print('array[i]', array[i])
        if (_min + array[i]) < result:
            result = _min + array[i]
            print('result', result)
        print()
    return result

# Example usage:
A = [5, 2, 4, 6, 3, 7]
print(solution(A))

# with checker(solution, repeat=1000, check_success=True) as c:
#     c.check_1([5, 2, 4, 6, 3, 7] + [1000] * 1000, 5)

with checker(minSum, repeat=0, check_success=True) as c:
    # c.check_1([5, 2, 4, 6, 3, 7] + [1000] * 1000, 5)
    c.check_1([5, 2, 4, 6, 3, 7], 5)
