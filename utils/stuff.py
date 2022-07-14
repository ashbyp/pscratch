import timeit
from functools import wraps


def measure(name):
    def decorate(func):
        @wraps(func)
        def _time_it(*args, **kwargs):
            start = timeit.default_timer()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = timeit.default_timer() - start
                print(f'Function:{name} elapsed seconds {elapsed}')
        return _time_it
    return decorate


class C:
    A: str = "hello"

    def __init__(self):
        self.A = 'selfA'
        C.A = 'classA'


if __name__ == '__main__':
    c = C()
    print(c.A)
    print(C.A)