Point = tuple[int, int] | list[int, int]
Line = tuple[Point, Point] | list[Point, Point]
Rect = tuple[Point, Point] | list[Point, Point]
Vector = tuple[Point] | list[Point]
PythonMatrix = list[list[int | float | None]]
PythonVector = list[int | float | None]


def draw_rect(rect: Rect) -> None:
    min_x = min(rect[0][0], rect[1][0])
    max_x = max(rect[0][0], rect[1][0])
    min_y = min(rect[0][1], rect[1][1])
    max_y = max(rect[0][1], rect[1][1])

    for x in range(min_x - 5, max_x + 5):
        for y in range(min_y - 5, max_y + 5):
            if min_x <= x <= max_x and min_y <= y <= max_y:
                print('*', end='')
            elif x == min_x - 5 or x == max_x + 4:
                print('_', end='')
            elif y == min_y - 5 or y == max_y + 4:
                print('|', end='')
            else:
                print('.', end='')
        print()
    print()


if __name__ == '__main__':
    r = ((1, 1), (5,5))
    draw_rect(r)