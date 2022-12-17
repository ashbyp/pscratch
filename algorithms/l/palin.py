class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''.join([x.lower() for x in s if x.isalnum()])
        return r == r[::-1]


def main():
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == '__main__':
    main()