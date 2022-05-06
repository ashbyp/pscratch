
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


if __name__ == '__main__':
    x=fib(100)
    x = filter(lambda x: x < 4000000 and x%2==0, x)
    print(sum(x))
