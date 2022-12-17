from utils.measure import checker


class Solution:

    def climbStairs(self, n: int) -> int:
        return 0


if __name__ == '__main__':
    with checker(Solution().climbStairs, repeat=1000, check_success=True) as c:
        c.check_1(2, 2)
        c.check_1(3, 3)

