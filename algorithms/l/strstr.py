class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+(len(needle))] == needle:
                return i
        return -1


    def strStr2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+(len(needle))] == needle:
                return i
        return -1


def main():
    print(Solution().strStr(haystack="a", needle="a"))
    print(Solution().strStr(haystack = "hello", needle = "ll"))
    print(Solution().strStr(haystack = "aaaaa", needle = "bba"))
    print(Solution().strStr(haystack="hello", needle="0"))
    print(Solution().strStr(haystack="aaaaa", needle=""))
    print(Solution().strStr(haystack="", needle="bba"))

    print('=' * 80)
    print(Solution().strStr1(haystack="a", needle="a"))
    print(Solution().strStr1(haystack="hello", needle="ll"))
    print(Solution().strStr1(haystack="aaaaa", needle="bba"))
    print(Solution().strStr1(haystack="hello", needle="0"))
    print(Solution().strStr1(haystack="aaaaa", needle=""))
    print(Solution().strStr1(haystack="", needle="bba"))


if __name__ == '__main__':
    main()

