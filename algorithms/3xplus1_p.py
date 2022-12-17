import multiprocessing as mp


def xxx_plus1(num):
    r = [num]
    n = num
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        r.append(n)
    return num, max(r), len(r)


if __name__ == '__main__':
    n, m, l = xxx_plus1(27)
    print(f'N: {n} Max: {m} Len: {l}')

    pool = mp.Pool(mp.cpu_count())

    r = []
    for n in range(1, 1000):
        r.append(xxx_plus1(n))
    print(r)

    print(f'{mp.cpu_count()} CPUs')

    r = [pool.apply(xxx_plus1, args=(n,)) for n in range(1, 1000)]
    print(r)