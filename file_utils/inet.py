import os.path
from urllib.error import URLError
from urllib.request import urlopen
from file_utils.misc import words_from_file

WORDY_URLS = [
    'https://www.w3.org/TR/PNG/iso_8859-1.txt',
    'https://www.ietf.org/rfc/rfc1950.txt',
    'http://www.ietf.org/rfc/rfc1123.txt',
    'https://www.wireshark.org/docs/man-pages/wireshark-filter.html',
    'http://tivo-mplayer.sourceforge.net/docs/mplayer-man.html'
]


def download_url(url, filename) -> bool:
    try:
        print(f'Downloading {url}')
        data = urlopen(url)
    except (ValueError, URLError) as e:
        print(f'Error downloading {url} - {e}')
        return False

    with open(filename, "w") as f:
        for line in data:
            f.write(line.decode('utf-8'))
    return True


def get_words(urls=None, unique=True) -> list[str]:
    if urls is None:
        urls = WORDY_URLS
    words = []
    for url in urls:
        filename = url.split('/')[-1] + '.downloaded'
        if not os.path.exists(filename):
            if not download_url(url, filename):
                continue
        doc_words = words_from_file(filename, '.html' in filename)
        if unique:
            doc_words = list(dict.fromkeys(doc_words))
        print(f'There were {len(doc_words)} words in {filename}')
        words += doc_words
    return words
