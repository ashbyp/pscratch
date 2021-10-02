def fib(n):
    if n < 1:
        raise ValueError("terms must be greater than zero")
    if n < 3:
        return 1
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    print(', '.join([str(fib(n)) for n in range(1, 20)]))




