from heapq import heappop, heappush

data="""2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

grid = list(map(list, data.splitlines()))
n_rows, n_cols = len(grid), len(grid[0])
t_row, t_col = n_rows - 1, n_cols - 1
seen = set()
start = (0, 0, 0, 0, 0, 0) # hl, r, c, dr, dc, num
pq =[]
heappush(pq, start)

while pq:
    hl, r, c, dr, dc, num = heappop(pq)
    if r < 0 or r > n_rows - 1 or c < 0 or c > n_cols - 1:
        continue

    if (t_row, t_col) == (r, c):
        print(hl)
        break






