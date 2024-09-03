import hashlib

pdata = "dmypynyp"

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
ROUTE_MAP = {0: 'U', 1: 'D', 2: 'L', 3: 'R'}
GRID_MAX_X, GRID_MAX_Y = 3, 3


def move(x: int, y: int, direction: int) -> tuple[int, int]:
    if direction == UP:
        return x, y - 1
    elif direction == DOWN:
        return x, y + 1
    elif direction == LEFT:
        return x - 1, y
    elif direction == RIGHT:
        return x + 1, y


def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:4]


def is_open(hashed: str, direction: int) -> bool:
    return hashed[direction] in ('b', 'c', 'd', 'e', 'f')


def get_candidate_moves(x: int, y: int, hashed: str) -> list[int]:
    candidates = []
    if y > 0 and is_open(hashed, UP):
        candidates.append(UP)
    if y < GRID_MAX_Y and is_open(hashed, DOWN):
        candidates.append(DOWN)
    if x > 0 and is_open(hashed, LEFT):
        candidates.append(LEFT)
    if x < GRID_MAX_X and is_open(hashed, RIGHT):
        candidates.append(RIGHT)
    return candidates


def part2(data: str):
    x, y = 0, 0
    all_routes, routes = [], []

    hashed = md5(data)
    candidates = get_candidate_moves(x, y, hashed)
    for c in candidates:
        routes.append((data + ROUTE_MAP[c], move(x, y, c)))

    while routes:
        p, (x, y) = routes.pop()

        if (x, y) == (GRID_MAX_X, GRID_MAX_Y):
            all_routes.append(p)
            continue

        hashed = md5(p)
        candidates = get_candidate_moves(x, y, hashed)
        for c in candidates:
            routes.append((p + ROUTE_MAP[c], move(x, y, c)))

    all_routes.sort(key=len)
    print(all_routes[0])
    print(all_routes[-1])
    print(len(all_routes[-1]) - len(data))


def main():
    part2(pdata)


if __name__ == '__main__':
    main()
