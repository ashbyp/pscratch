import json
from typing import List, ClassVar
from dataclasses import dataclass, field


@dataclass
class Config:
    name: str
    age: int
    level: int
    words: List[str] = field(default_factory=list)
    cvar: ClassVar[float] = 0.5


def debug(*args, **kwargs):
    print('Args\n', args)
    print('KWArgs\n', kwargs)


def read_config(filename):
    with open(filename, "r") as file:
        print('---')
        debug(**json.load(file))
        print('---')
    with open(filename, "r") as file:
        return Config(**json.load(file))


if __name__ == '__main__':
    c = read_config('config.json')
    print(c)
    print(c.age)
    print(Config.cvar)

