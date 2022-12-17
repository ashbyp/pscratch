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
                    dfs(i, j)
                    islands += 1
        return islands


if __name__ == '__main__':
    with checker(Solution().numIslands, repeat=1000, check_success=True) as c:
        i = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]

        c.check_1(i, 1)

        i = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]

        c.check_1(i, 3)
