class Solution:

    def to_int(self, digits: list[int]) -> int:
        m = 1
        v = 0
        for x in digits[::-1]:
            v += x * m
            m *= 10
        return v

    def to_array(self, v: int) -> list[int]:
        a = []
        while v:
            a.insert(0, v % 10)
            v = v // 10
        return a


    def plusOne(self, digits: list[int]) -> list[int]:
        ls = len(digits) - 1
        if digits and digits[ls] < 9:
            digits[ls] = digits[ls] + 1
            return digits

        v = self.to_int(digits)
        return self.to_array(v + 1)

    


def main():
    print(Solution().plusOne([1,2,3]))
    print(Solution().plusOne([4,3,2,1]))
    print(Solution().plusOne([9]))


if __name__ == '__main__':
    main()