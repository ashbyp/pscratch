import os
import random
import re
from collections import namedtuple, defaultdict

from algorithms.aoc.utils import launch_chrome, aoc_url, read_file, write_file

Puzzle = namedtuple('Puzzle', ['year', 'day'])


def not_completed() -> Puzzle:
    all_puzzles = set(range(1, 26))
    for name in os.listdir():
        if os.path.isdir(name) and re.match(r"\d{4}", name):
            complete = {int(f.replace('.py', '')) for f in os.listdir(name) if re.match(r'\d{1,2}\.py', f)}
            for t in all_puzzles.difference(complete):
                yield Puzzle(year=int(name), day=t)


def create_file(suggest: Puzzle):
    print(f'Creating: {suggest.year}/{suggest.day}.py')
    write_file(
        read_file('template.py').replace("<<URL>>", aoc_url(suggest.year, suggest.day)),
        f'{suggest.year}/{suggest.day}.py')


def suggest_puzzle(max_day=25, exclude_years=None) -> None:
    suggest = random.choice(
        [choice for choice in not_completed() if choice.day <= max_day and choice.year not in exclude_years])
    print('Suggestion')
    print(f'Year: {suggest.year} Day: {suggest.day}')

    create = None
    while create is None:
        user_input = input(f'Create template? ([y]/n) {aoc_url(suggest.year, suggest.day)}').strip().lower()
        if user_input == 'n' or not user_input:
            create = False
        elif user_input == 'y':
            create = True
        else:
            print('** invalid')

    if create:
        create_file(suggest)
        launch_chrome(suggest.year, suggest.day)


def show_incomplete():
    incomplete = defaultdict(list)
    min_year = float('inf')
    max_year = 0

    for year, day in not_completed():
        incomplete[year].append(day)
        min_year = min(min_year, year)
        max_year = max(max_year, year)

    print()
    for year in range(min_year, max_year + 1):
        print(f'{year}:  ', end='')
        for day in range(1, 26):
            if day in incomplete[year]:
                print(f'   ', end='')
            else:
                print(f' {day:2}', end='')
        print()

def create_next(year: int):
    not_complete = sorted(
        filter(lambda p: p.year == year, not_completed()),
        key=lambda p: p.year
    )
    create_file(not_complete.pop(0))


if __name__ == '__main__':
    # show_incomplete()
    # print()
    # suggest_puzzle(18, [2023])
    create_next(2024)
