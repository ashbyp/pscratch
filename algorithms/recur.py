
def reduce_by_one(x):
    print('before', x)
    if x >= 0:
        reduce_by_one(x-1)
        print('inside', x)
    print('after', x)

# 1 1 2 3 5 8 13 21 34

def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)


print(fib(8))