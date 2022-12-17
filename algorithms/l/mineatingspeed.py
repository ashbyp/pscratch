from utils.measure import checker

class Solution:

    def minEatingSpeed(self, piles: list[int], H: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l <= r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ((p - 1) // m) + 1
            if totalTime <= H:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k


def main():
    with checker(Solution().minEatingSpeed, repeat=1_000_000) as c:
        c.check_2([3,6,7,11], 8, 4)
        c.check_2([30,11,23,4,20], 5, 30)


if __name__ == '__main__':
    main()



