import os
import webbrowser

import requests


def get_data(year: int, day: int) -> str:
    filename = f'data/{day}.txt'
    if os.path.exists(filename):
        return read_file(filename)

    url = f'https://adventofcode.com/{year}/day/{day}/input'
    data = download_webpage(url)
    os.makedirs('data')
    write_file(data, filename)
    return data


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except IOError as e:
        print(f"Error reading the file: {e}")
        return None


def download_instructions(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}'
    data = download_webpage(url)
    return data


def aoc_url(year: int, day: int) -> str:
    return f'https://adventofcode.com/{year}/day/{day}'


def launch_chrome(year: int, day: int) -> None:
    url = aoc_url(year, day)
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    print(f'Launched: {url}')


def download_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the webpage: {e}")
        return None


def get_adjacent(point: tuple[int, int]) -> list[tuple[int, int]]:
    points = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            points.append((point[0] + dx, point[1] + dy))
    return points


def get_positive_adjacent(point: tuple[int, int]) -> list[tuple[int, int]]:
    points = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = point[0] + dx, point[1] + dy
            if nx >= 0 and ny >= 0:
                points.append((nx, ny))
    return points


def to_grid(points: tuple[int, int], occupied_str: str = 'X') -> list[list[str]]:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    min_x -= 3
    max_x += 3
    min_y -=3
    max_y += 3
    grid = []
    m = 1
    for y in range(min_y, max_y):
        row = []
        for x in range(min_x, max_x):
            if (x, y) in points:
                print('at ', (x, y))
                row.append(str(m))
                m += 1
            else:
                row.append(' ')
        grid.append(row)
    return grid


def write_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
    except IOError as e:
        print(f"Error saving the content to file: {e}")


if __name__ == '__main__':
    pts = get_adjacent((4, 5))
    print(pts)
    for r in to_grid(pts):
        print(r)
    pts = get_positive_adjacent((0, 0))
    print(pts)
    for r in to_grid(pts):
        print(r)

