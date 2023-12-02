def solution(A, R):
    max_items = 0
    for i in range(len(A) - R + 1):
        shelves = A[0:i] + A[i+R:]
        max_items = max(max_items, len(set(shelves)))
    return max_items


A = [2, 1, 2, 3, 2, 2]
R = 3
result = solution(A, R)
print(result)
