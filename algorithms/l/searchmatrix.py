
class Solution:

    def bin_search(self, nums: list[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            m = (last + first) // 2
            if nums[m] > target:
                last = m - 1
            elif nums[m] < target:
                first = m + 1
            else:
                return nums[m]
        return -1

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flat = [j for sub in matrix for j in sub]
        return self.bin_search(flat, target) != -1

def main():
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11))
    print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))


if __name__ == '__main__':
    main()