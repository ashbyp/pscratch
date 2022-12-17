class Solution:

    def maxArea(self, height: list[int]) -> int:
        m=0
        for i, h in enumerate(height):
            for j in range(i + 1, len(height)):
                a = (j - i) * min(height[i], height[j])
                if a > m:
                    m = a
        return m


def main():
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))


if __name__ == '__main__':
    main()