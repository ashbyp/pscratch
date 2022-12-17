class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1


def main() -> None:
    x = [1, 1, 2]
    k = Solution().removeDuplicates(x)
    print(x[0:k])
    x = [0,0,1,1,1,2,2,3,3,4]
    k = Solution().removeDuplicates(x)
    print(x[0:k])

if __name__ == '__main__':
    main()

