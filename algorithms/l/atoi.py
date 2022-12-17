from typing import List
from utils.measure import checker


class Solution:

    def myAtoi(self, s: str) -> int:
        ans = 0
        pos = True
        started = False

        for c in s:
            if c == ' ':
                if started:
                    break
            elif c == '-':
                if started:
                    break
                else:
                    pos = False
                    started = True
            elif c == '+':
                if started:
                    break
                else:
                    pos = True
                    started = True
            elif c.isdigit():
                if not ans:
                    ans = int(c)
                else:
                    ans = 10 * ans + int(c)
                started = True
            else:
                break

        if not pos:
            ans = -ans

        if ans < -2**31:
            return -2**31
        if ans > 2**31 - 1:
            return 2**31 - 1

        return ans






if __name__ == '__main__':
    with checker(Solution().myAtoi, repeat=1000, check_success=True) as c:
        c.check_1('42', 42)
        c.check_1('-42', -42)
        c.check_1("4193 with words", 4193)
        c.check_1('+1', 1)


