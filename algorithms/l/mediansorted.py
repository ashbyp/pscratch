from typing import List
from utils.measure import checker


class Solution:

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1 + nums2)
        l = len(x)
        if l % 2 == 0:
            return (x[l // 2] + x[(l // 2) - 1]) / 2
        else:
            return x[l // 2]




if __name__ == '__main__':
    with checker(Solution().findMedianSortedArrays1, repeat=1000, check_success=True) as c:
        c.check_2([1, 3], [2], 2)
        c.check_2([1, 2], [3, 4], 2.5)
