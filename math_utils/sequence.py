from typing import Callable


def find_nth_term(start: int, nth: int, next_fn: Callable[[int], int]) -> int:
    t = start
    for _ in range(1, nth):
        t = next_fn(t)
    return t


def main():
    print(f'4, 7, 11, 14 ... 20th is: {find_nth_term(4, 20, lambda x: x+3)}')
    print(f'2, 8, 14, 20 ... 20th is: {find_nth_term(2, 50, lambda x: x+6)}')


if __name__ == '__main__':
    main()