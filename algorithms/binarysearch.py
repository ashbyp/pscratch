import random
from utils.measure import timefunc

@timefunc('search')
def binsearch(l, n):
    first, last = (0, len(l) -1)
    while first <= last:
        m = (last + first) // 2
        if l[m] == n:
            return m
        if l[m] > n:
            last = m - 1
        else:
            first = m + 1
    return None


def main():
    MAX = 200000
    a = {random.randint(1, MAX) for _ in range(MAX)}
    a = sorted(list(a))
    i = [x for x in range(len(a))]
    # print('Index: ', [f'{x:2d}' for x in i])
    # print('Array: ', [f'{x:2d}' for x in a])

    for t in range(10):
        n = random.randint(0, MAX)
        i = binsearch(a, n)
        print(f'Index of {n} is {i}, check={a[i] if i else None}')


if __name__ == '__main__':
    main()