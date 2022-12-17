
def boundedSlicesSlow(K, A):
    N= len(A)
    result = 0
    for i in range(N):
        minimum = A[i]
        maximum = A[i]
        for j in range(i, N):
            print(f'check {i}, {j}')
            maximum = max(maximum, A[j])
            minimum = min(minimum, A[j])
            if maximum - minimum <= K:
                result += 1
                if result == 10e9:
                    return result
            else:
                break
    return result


if __name__ == '__main__':
    print(boundedSlicesSlow(2, [3, 5, 7, 6, 3]))