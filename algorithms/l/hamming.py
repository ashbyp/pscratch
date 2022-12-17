class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(x) for x in f'{n:b}')


def main() -> None:
    print(Solution().hammingWeight(10))


if __name__ == '__main__':
    main()

