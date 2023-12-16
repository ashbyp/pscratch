from dataclasses import dataclass


def read_data(filename) -> str:
    with open(filename) as f:
        return f.read().strip()


# data=read_data('16_test_data.txt')
# data=read_data('16_my_test_data.txt')
data=read_data('16_puzzle_data.txt')


UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


@dataclass(frozen=True)
class Sprite:
    row: int
    col: int
    direction: int

    move_map = {
        UP: (-1, 0),
        DOWN: (1, 0),
        LEFT: (0, -1),
        RIGHT: (0, 1),
    }

    @staticmethod
    def move(sprite: 'Sprite', direction: int):
        move = Sprite.move_map[direction]
        return Sprite(sprite.row + move[0], sprite.col + move[1], direction)


OBSTACLE_MAP = {
        '.': {
                UP:    [UP],
                DOWN:  [DOWN],
                LEFT:  [LEFT],
                RIGHT: [RIGHT],
        },
        '/': {
                UP:    [RIGHT],
                DOWN:  [LEFT],
                LEFT:  [DOWN],
                RIGHT: [UP],
        },
        '\\': {
                UP:    [LEFT],
                DOWN:  [RIGHT],
                LEFT:  [UP],
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
        current_pos = queue.pop()
        if not (0 <= current_pos.row < n_rows and 0 <= current_pos.col < n_cols) or current_pos in illuminated:
            continue

        illuminated.add(current_pos)
        obstacle = grid[current_pos.row][current_pos.col]

        directions = OBSTACLE_MAP[obstacle]
        for direction in directions[current_pos.direction]:
            queue.append(Sprite.move(current_pos, direction))

    return len(set((s.row, s.col) for s in illuminated))


def part1():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')
    print(shine_beam(grid, (Sprite(0, 0, RIGHT))))


def part2():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')

    max_illuminated = 0

    for r in range(n_rows):
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(r, 0, RIGHT))))
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(r, n_cols - 1, LEFT))))

    for c in range(n_cols):
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(0, c, DOWN))))
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(n_rows - 1, c, UP))))

    print(max_illuminated)


if __name__ == '__main__':
    from utils.measure import timeblock
    with timeblock():
        part1()
    with timeblock():
        part2()
