

def xxx_plus_1(n):
    r = [n]
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        r.append(n)
    return r


if __name__ == '__main__':
    for n in range(10000, 10100):
        results = xxx_plus_1(n)
        print(f'N: {n}\tMax: {max(results)}\t\tLen: {len(results)}')

    print('-' * 100)

    max_len = 0
    for n in range(1, 1000000000000000000000):
        results = xxx_plus_1(n)
        l = len(results)
        if l > max_len:
            max_len = l
            print(f'N: {n} has length of {l}')


