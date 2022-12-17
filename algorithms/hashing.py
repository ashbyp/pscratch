import hashlib
from statistics import mean
from typing import Any
from typing import Callable

import matplotlib.pyplot as plt
from scipy.stats import norm

from file_utils.inet import get_words
from math_utils.nputils import scale_values


def distribute(words: list[str], buckets: int, hash_func: Callable[[str], int] = hash) -> [list[list], int, int]:
    d = [[] for _ in range(buckets)]
    min_hash, max_hash = None, None
    for word in words:
        h = hash_func(word)
        if not min_hash or h < min_hash:
            min_hash = h
        if not max_hash or h > max_hash:
            max_hash = h
        h %= buckets
        d[h].append(word)
    return d, min_hash, max_hash


def md5_hash(s: str) -> int:
    h = hashlib.md5(s.encode('utf-8'))
    return int.from_bytes(h.digest()[0:3], 'big')


def sha256_hash(s: str) -> int:
    h = hashlib.sha256(s.encode('utf-8'))
    return int.from_bytes(h.digest()[0:3], 'big')


def silly_hash(s: str) -> int:
    return sum(ord(c)**2 for c in s)


def distribute_hash_function(name: str, words: list[str], hash_buckets: int,
                             hash_func: Callable[[str], int], chart_buckets: int, chart: Any) -> None:
    print(f'Distributing {name} hash func with {hash_buckets} buckets:')
    d, min_hash, max_hash = distribute(words, hash_buckets, hash_func)
    print(f'Buckets full={sum(1 for x in d if x)}, Min hash={min_hash}, Max hash={max_hash}')
    sz = [len(x) for x in d]
    print(f'{sz[0:100]}...' if len(sz) > 100 else sz)
    mu, sigma = norm.fit(sz)
    print(f'Sum={sum(sz)}, Max={max(sz)}, min={min(sz)}, Mean={mean(sz)}, Mu={mu}, sigma={sigma}')
    chart.set_title(name)
    n, bins, patches = chart.hist(sz, chart_buckets, facecolor='red', alpha=0.5)
    best_fit_line = norm.pdf(bins, mu, sigma)
    chart.plot(bins, scale_values(best_fit_line, n), color='black', linestyle='dashed')


def main() -> None:
    words = get_words(unique=True)
    print(f'Testing {len(words)} words')
    hash_buckets = 200
    chart_buckets = 20
    funcs = [(hash, 'Built-in'), (md5_hash, 'MD5'), (sha256_hash, 'SHA256'), (silly_hash, 'Silly')]

    _, axs = plt.subplots(len(funcs))
    chart = 0
    for func, name in funcs:
        distribute_hash_function(name, words, hash_buckets, func, chart_buckets, axs[chart])
        chart += 1
    plt.show()


if __name__ == '__main__':
    main()
