from utils.measure import checker


class Solution:
    def fib(self, n: int) -> int:
        v = [0, 1]
        if n < 2: return v[n]
        for i in range(2, n+1):
            v.append(v[i-1] + v[i-2])
        return v[-1]


if __name__ == '__main__':
    with checker(Solution().fib, repeat=1000, check_success=True) as c:
        c.check_1(2, 1)
        c.check_1(3, 2)
        c.check_1(4, 3)
        c.check_1(5, 5)
        c.check_1(6, 8)