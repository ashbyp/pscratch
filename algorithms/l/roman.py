from utils.measure import checker


class Solution:
    def romanToInt1(self, s: str) -> int:
        vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        p = 0
        t = 0
        while p < len(s):
            if (p != len(s) - 1) and vals[s[p]] < vals[s[p+1]]:
                t += vals[s[p+1]] - vals[s[p]]
                p += 2
            else:
                t += vals[s[p]]
                p += 1
        return t

    def romanToInt2(self, s: str) -> int:
        sym = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        prev = 0

        for c in reversed(s):
            if sym[c] >= prev:
                result += sym[c]
            else:
                result -= sym[c]
            prev = sym[c]

        return result


if __name__ == '__main__':
    with checker(Solution().romanToInt1) as c:
        c.check_1('III', 3)
        c.check_1('LVIII', 58)
        c.check_1('MCMXCIV', 1994)
        c.check_1('M', 1000)
    with checker(Solution().romanToInt2) as c:
        c.check_1('III', 3)
        c.check_1('LVIII', 58)
        c.check_1('MCMXCIV', 1994)
        c.check_1('M', 1000)