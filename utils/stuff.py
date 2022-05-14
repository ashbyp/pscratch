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
