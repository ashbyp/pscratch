# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
# which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:

    def sum_squares(self, n):
        s = 0
        while n:
            s += (n % 10) ** 2
            n = n // 10
        return s


    def isHappy(self, n: int) -> bool:
        values = set()
        while n not in values:
            values.add(n)
            s = self.sum_squares(n)
            if s == 1:
                return True
            n = s
        return False


def main():
    print(Solution().isHappy(19)) # true
    print(Solution().isHappy(2)) # false


if __name__ == '__main__':
    main()