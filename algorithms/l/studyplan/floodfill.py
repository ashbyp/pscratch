from typing import List
from utils.measure import checker


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])
        replace = image[sr][sc]

        if replace == color:
            return image

        def fill(grid, row, col):
            if row < 0 or row > rows - 1 or col < 0 or col > cols - 1 or grid[row][col] != replace:
                return
            grid[row][col] = color

            fill(grid, row + 1, col)
            fill(grid, row - 1, col)
            fill(grid, row , col + 1)
            fill(grid, row, col - 1)

        fill(image, sr, sc)
        return image


if __name__ == '__main__':
    with checker(Solution().floodFill, repeat=1000, check_success=True) as c:
        c.check_4([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]])
        c.check_4([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]])
