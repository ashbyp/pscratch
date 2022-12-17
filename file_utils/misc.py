import math
import os
import re
from bs4 import BeautifulSoup


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def get_size(full_path: str, eat_exceptions:bool = True) -> int:
    try:
        return os.path.getsize(full_path)
    except OSError as e:
        if not eat_exceptions:
            print(e)
    return 0


def words_from_file(filename: str, is_html=False) -> list[str]:
    with open(filename, "r") as f:
        contents = f.read()
    if is_html:
        bs = BeautifulSoup(contents, 'html.parser')
        contents = bs.get_text()
    words = list(filter(lambda x: x, re.split('[ \n]', contents)))
    return words
