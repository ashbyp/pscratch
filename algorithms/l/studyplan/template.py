from typing import List
from utils.measure import checker


class Solution:

    def func(self, nums: List[int]) -> List[int]:
        return nums if nums[0] == 1 else []


if __name__ == '__main__':
    with checker(Solution().func, repeat=1000, check_success=True) as c:
        c.check_1([1,2,3,4], [1,3,6,10])
        c.check_1([1, 1, 1, 1, 1], [1, 2, 3, 4, 5])
        c.check_1([3,1,2,10,1], [3,4,6,16,17])

