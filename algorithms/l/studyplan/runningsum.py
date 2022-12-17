from typing import List
from utils.measure import checker

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[i-1] + nums[i])
        return res


if __name__ == '__main__':
    with checker(Solution().runningSum) as t:
        t.check_1([1,2,3,4], [1,3,6,10])
        t.check_1([1, 1, 1, 1, 1], [1, 2, 3, 4, 5])
        t.check_1([3,1,2,10,1], [3,4,6,16,17])

