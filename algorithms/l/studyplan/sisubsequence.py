from utils.measure import checker


class Solution:

    def isSubsequence1(self, s: str, t: str) -> bool:
        if s == t:
            return True

        pt = 0
        found = 0
        for c in s:
            while pt != len(t):
                if t[pt] == c:
                    pt += 1
                    found += 1
                    break
                else:
                    pt += 1

        return found == len(s)


if __name__ == '__main__':
    with checker(Solution().isSubsequence1, repeat=1000, check_success=True) as c:
        c.check_2('abc', 'ahbgdc', True)
        c.check_2('axc', 'ahbgdc', False)
        c.check_2('', '', True)

