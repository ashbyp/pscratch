import hashlib
from typing import List, Tuple

pdata = "dmypynyp"

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}
GRID_MAX_X, GRID_MAX_Y = 3, 3


def move(x: int, y: int, direction: str) -> Tuple[int, int]:
    dx, dy = DIRECTIONS[direction]
    return x + dx, y + dy


def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:4]


def is_open(hashed: str, direction: str) -> bool:
    return hashed['UDLR'.index(direction)] in 'bcdef'


def get_candidate_moves(x: int, y: int, hashed: str) -> List[str]:
    boundaries = {
        'U': y > 0,
        'D': y < GRID_MAX_Y,
        'L': x > 0,
        'R': x < GRID_MAX_X
    }
    return [
        direction for direction in 'UDLR'
        if boundaries[direction] and is_open(hashed, direction)
    ]


def add_candidates_to_routes(data: str, x: int, y: int, routes: List[Tuple[str, Tuple[int, int]]]):
    hashed = md5(data)
    for direction in get_candidate_moves(x, y, hashed):
        routes.append((data + direction, move(x, y, direction)))


def solution(data: str):
    routes = []
    add_candidates_to_routes(data, 0, 0, routes)
    all_routes = []

    while routes:
        path, (x, y) = routes.pop()

        if (x, y) == (GRID_MAX_X, GRID_MAX_Y):
            all_routes.append(path)
        else:
            add_candidates_to_routes(path, x, y, routes)

    all_routes.sort(key=len)
    print(f"Shortest path: {all_routes[0]}")
    print(f"Longest path: {all_routes[-1]}")
    print(f"Length of longest path: {len(all_routes[-1]) - len(data)}")


def main():
    solution(pdata)


if __name__ == '__main__':
    main()
