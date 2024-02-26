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


def write_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
    except IOError as e:
        print(f"Error saving the content to file: {e}")


if __name__ == '__main__':
    print(download_webpage('https://adventofcode.com/2018/day/1/input'))
