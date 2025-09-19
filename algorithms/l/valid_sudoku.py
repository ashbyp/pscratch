from typing import List


class Solution:
    def dups(self, l1: list[str]) -> bool:
        seen = set([])
        for l in l1:
            if l != '.' and l in seen:
                return True
            seen.add(l)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for row in board:
            if self.dups(row):
                # print(f'Dupe row  {row}')
                return False

        # cols
        for c in range(9):
            l = [board[r][c] for r in range(0, 9)]
            if self.dups(l):
                # print(f'Dupe col  {l}')
                return False

        # boxes
        for ro in range(0, 9, 3):
            for co in range(0, 9, 3):
                l = [board[r + ro][c + co] for r in range(3) for c in range(3)]
                if self.dups(l):
                    # print(f'Dupe box {l}')
                    return False

        return True


if __name__ == '__main__':
    input = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    print(s.isValidSudoku(input))

    input = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    print(s.isValidSudoku(input))
