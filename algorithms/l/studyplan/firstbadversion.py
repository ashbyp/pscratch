from utils.measure import checker

BAD = 4


def isBadVersion(version: int) -> bool:
    return version >= BAD


class Solution:

    def firstBadVersion(self, n):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    with checker(Solution().firstBadVersion, repeat=0, check_success=True) as c:
        BAD = 4
        c.check_1(6, BAD)

