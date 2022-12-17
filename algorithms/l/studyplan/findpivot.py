from typing import List
from utils.measure import checker


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums)

        for i in range(len(nums)):
            if i > 0:
                sum_left = sum_left + nums[i - 1]

            sum_right = sum_right - nums[i]

            if sum_left == sum_right:
                return i

        return -1


if __name__ == '__main__':
    with checker(Solution().pivotIndex, repeat=10000, check_success=True) as c:
        c.check_1([1,7,3,6,5,6], 3)
        c.check_1([1,2,3], -1)
        c.check_1([2,1,-1], 0)

