from dataclasses import dataclass
from enum import Enum


def read_data(filename) -> str:
    with open(filename) as f:
        return f.read().strip()


# data=read_data('16_test_data.txt')
# data=read_data('16_my_test_data.txt')
data=read_data('16_puzzle_data.txt')


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


@dataclass(frozen=True)
class Sprite:
    row: int
    col: int
    direction: Direction

    @staticmethod
    def move(sprite: 'Sprite', direction: Direction):
        direction_map = {
            Direction.UP: (sprite.row - 1, sprite.col),
            Direction.DOWN: (sprite.row + 1, sprite.col),
            Direction.LEFT: (sprite.row, sprite.col - 1),
            Direction.RIGHT: (sprite.row, sprite.col + 1)
        }

        if direction in direction_map:
            new_row, new_col = direction_map[direction]
            return Sprite(new_row, new_col, direction)
        else:
            raise ValueError('Invalid direction')


def shine_beam(grid, start_pos):
    n_rows, n_cols = len(grid), len(grid[0])
    illuminated = [[set([]) for _ in range(n_cols)] for _ in range(n_rows)]
    queue = [start_pos]

    while True and len(queue):
        current_pos = queue.pop()
        if not (0 <= current_pos.row < n_rows and 0 <= current_pos.col < n_cols) or current_pos in illuminated[current_pos.row][current_pos.col]:
            continue

        illuminated[current_pos.row][current_pos.col].add(current_pos)
        obstacle = grid[current_pos.row][current_pos.col]

        obstacle_map = {
            '.': {
                    Direction.UP:    [current_pos.direction],
                    Direction.DOWN:  [current_pos.direction],
                    Direction.LEFT:  [current_pos.direction],
                    Direction.RIGHT: [current_pos.direction],
            },
            '/': {
                    Direction.UP:    [Direction.RIGHT],
                    Direction.DOWN:  [Direction.LEFT],
                    Direction.LEFT:  [ Direction.DOWN],
                    Direction.RIGHT: [ Direction.UP],
            },
            '\\': {
                    Direction.UP:    [Direction.LEFT],
                    Direction.DOWN:  [Direction.RIGHT],
                    Direction.LEFT:  [Direction.UP],
                    Direction.RIGHT: [Direction.DOWN],
            },
            '|': {
                Direction.UP: [current_pos.direction],
                Direction.DOWN: [current_pos.direction],
                Direction.LEFT: [Direction.UP, Direction.DOWN],
                Direction.RIGHT: [Direction.UP, Direction.DOWN],
            },
            '-': {
                Direction.UP: [Direction.LEFT, Direction.RIGHT],
                Direction.DOWN: [Direction.LEFT, Direction.RIGHT],
                Direction.LEFT: [current_pos.direction],
                Direction.RIGHT: [current_pos.direction],
            },
        }

        directions = obstacle_map[obstacle]
        for direction in directions[current_pos.direction]:
            queue.append(Sprite.move(current_pos, direction))

    return sum(1 for row in range(n_rows) for col in range(n_cols) if illuminated[row][col])


def part1():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')
    print(shine_beam(grid, (Sprite(0, 0, Direction.RIGHT))))


def part2():
    grid = list(map(list, data.splitlines()))
    n_rows, n_cols = len(grid), len(grid[0])
    print(f'Rows {n_rows}, Cols {n_cols}')

    max_illuminated = 0

    for r in range(n_rows):
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(r, 0, Direction.RIGHT))))
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(r, n_cols - 1, Direction.LEFT))))

    for c in range(n_cols):
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(0, c, Direction.DOWN))))
        max_illuminated = max(max_illuminated, shine_beam(grid, (Sprite(n_rows - 1, c, Direction.UP))))

    print(max_illuminated)


if __name__ == '__main__':
    part1()
    part2()
