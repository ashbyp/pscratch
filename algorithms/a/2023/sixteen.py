def read_data(filename) -> str:
    with open(filename) as f:
        return f.read().strip()


# data=read_data('16_test_data.txt')
# data=read_data('16_my_test_data.txt')
data = read_data('16_puzzle_data.txt')

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

MOVE_MAP = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}

OBSTACLE_MAP = {
    '.': {
        UP: [UP],
        DOWN: [DOWN],
        LEFT: [LEFT],
        RIGHT: [RIGHT],
    },
    '/': {
        UP: [RIGHT],
        DOWN: [LEFT],
        LEFT: [DOWN],
        RIGHT: [UP],
    },
    '\\': {
        UP: [LEFT],
        DOWN: [RIGHT],
        LEFT: [UP],
        RIGHT: [DOWN],
    },
    '|': {
        UP: [UP],
        DOWN: [DOWN],
        LEFT: [UP, DOWN],
        RIGHT: [UP, DOWN],
    },
    '-': {
        UP: [LEFT, RIGHT],
        DOWN: [LEFT, RIGHT],
        LEFT: [LEFT],
        RIGHT: [RIGHT],
    },
}


def shine_beam(grid, start_pos):
    n_rows, n_cols = len(grid), len(grid[0])
    illuminated = set()
    queue = [start_pos]

    while len(queue):
        pos = queue.pop()
        if not (0 <= pos[0] < n_rows and 0 <= pos[1] < n_cols) or pos in illuminated:
            continue

        illuminated.add(pos)
        obstacle = grid[pos[0]][pos[1]]
        directions = OBSTACLE_MAP[obstacle]

        for direction in directions[pos[2]]:
            move = MOVE_MAP[direction]
            queue.append((pos[0] + move[0], pos[1] + move[1], direction))

    return len(set((i[0], i[1]) for i in illuminated))


def part1():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')
    print(shine_beam(grid, (0, 0, RIGHT)))


def part2():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')

    max_illuminated = 0

    for r in range(n_rows):
        max_illuminated = max(max_illuminated, shine_beam(grid, (r, 0, RIGHT)))
        max_illuminated = max(max_illuminated, shine_beam(grid, (r, n_cols - 1, LEFT)))

    for c in range(n_cols):
        max_illuminated = max(max_illuminated, shine_beam(grid, (0, c, DOWN)))
        max_illuminated = max(max_illuminated, shine_beam(grid, (n_rows - 1, c, UP)))

    print(max_illuminated)


if __name__ == '__main__':
    from utils.measure import timeblock

    with timeblock():
        part1()
    with timeblock():  # 7 secs
        part2()
