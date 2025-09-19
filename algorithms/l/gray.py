from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:

        '''
        An n-bit gray code sequence is a sequence of 2n integers where:

        Every integer is in the inclusive range [0, 2n - 1],
        The first integer is 0,
        An integer appears no more than once in the sequence,
        The binary representation of every pair of adjacent integers differs by exactly one bit, and
        The binary representation of the first and last integers differs by exactly one bit.'''

        can_use = {x for x in range(0, (n**2 - 1) + 1)}
        print(f'I can use {can_use}')

        for i in can_use:
            print(f'{x:b}')



        return []


if __name__ == '__main__':
    s = Solution()
    print(f'Ans for 2 is {s.grayCode(2)}')
    print(f'Ans for 4 is {s.grayCode(4)}')
    print(f'Ans for 10 is {s.grayCode(10)}')
