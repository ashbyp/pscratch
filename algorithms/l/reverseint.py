from typing import List
from utils.measure import checker


class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        if neg:
            x = -x

        ans = 0
        while x:
            y = x % 10
            x = x // 10
            if not ans:
                ans = y
            else:
                ans = 10 * ans + y

        if ans > 2**31-1 or ans < -2**31:
            return 0

        return -ans if neg else ans


if __name__ == '__main__':
    with checker(Solution().reverse, check_success=True) as c:
        c.check_1(123, 321)
        c.check_1(-123, -321)
        c.check_1(120, 21)

