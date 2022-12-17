from utils.measure import timeblock


def fib(n):
    if n < 1:
        raise ValueError("terms must be greater than zero")
    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)


def fibi(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 1

    v0 = 1
    v1 = 1
    x = 0
    for i in range(3, n+1):
        x = v0 + v1
        v1 = v0
        v0 = x
    return x


def fib_dp(n: int) -> int:
    v = [0, 1]
    if n < 2: return v[n]
    for i in range(2, n+1):
        v.append(v[i-1] + v[i-2])
    return v[-1]


if __name__ == '__main__':
    print(fib(5))


    with timeblock('recur'):
        print(fib(1))
        print(fib(2))
        print(fib(3))
        print(fib(4))
        print(fib(35))

    with timeblock('iter'):
        print(fibi(1))
        print(fibi(2))
        print(fibi(3))
        print(fibi(4))
        print(fibi(35))

    with timeblock('dp'):
        print(fib_dp(1))
        print(fib_dp(2))
        print(fib_dp(3))
        print(fib_dp(4))
        print(fib_dp(35))

