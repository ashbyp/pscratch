from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        f = 0
        while i < len(nums):
            if nums[i] == val:
                j = len(nums) - 1
                while nums[j] == val:
                    j -= 1
                nums[i] = nums[j]
            else:
                f += 1
            i += 1
        return f

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], val = 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], val = 2))