from utils.measure import checker


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        l = 0
        o = 0
        for n in freq.values():
            if n % 2 == 0:
                l += n
            else:
                o += 1
                l += 2 * (n // 2)
        if o:
            l += 1
        return l



if __name__ == '__main__':
    with checker(Solution().longestPalindrome, repeat=10000) as c:
        c.check_1('abccccdd', 7)
        c.check_1('a', 1)
        c.check_1('bb', 2)