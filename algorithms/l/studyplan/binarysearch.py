from typing import List
from utils.measure import checker


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                left = m + 1
            else:
                right = m - 1

        return -1


if __name__ == '__main__':
    with checker(Solution().search, repeat=1000, check_success=True) as c:
        c.check_2([-1,0,3,5,9,12], 9, 4)
        c.check_2([-1,0,3,5,9,12], 2, -1)
        c.check_2([5], 5, 0)

