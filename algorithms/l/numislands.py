# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

from utils.measure import checker

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            # print (f' --> visit {i},{j}')
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        islands = 0
        for i in range(rows):
            for j in range(columns):
                if not visited[i][j] and grid[i][j] == '1':
                    #print(f'start dfs at {i},{j}')
                    dfs(i, j)
                    islands += 1
        return islands


def main():
    with checker(Solution().numIslands, repeat=1000) as c:
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        c.check_1(grid, 1)
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        c.check_1(grid, 3)


if __name__ == '__main__':
    main()