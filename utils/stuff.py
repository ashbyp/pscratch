import timeit
from functools import wraps


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = timeit.default_timer()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = timeit.default_timer() - start
            print(f'Elapsed seconds {elapsed}')
    return _time_it
