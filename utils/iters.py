import math
from typing import Callable


def test_fun(range_fn: Callable = range):
    x = 0
    for i in range_fn(1000):
        for j in range_fn(1000):
            x += math.sqrt(i * j)
    return x


def float_range(start: int | float, stop: int | float | None = None, step: int | float | None = None):
    # if set start=0.0 and step = 1.0 if not specified
    start = float(start)
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


def main():
    print(test_fun(range_fn=range))
    print(test_fun(range_fn=float_range))


if __name__ == '__main__':
    main()
