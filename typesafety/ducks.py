from typing import Protocol


class Fred(Protocol):
    def tom(self) -> str:
        ...

    def dick(self, a: str) -> str:
        ...


class Harry(Fred):
    def tom1(self) -> str:
        return 'tom'

    def dick(self, a: str) -> str:
        return 'dick ' + a


class Foo:
    def tom(self):
        return 'tom'

    def dick(self, a):
        return 'dick ' + a


def play(e: Fred):
    print(e.tom(), e.dick('harry'))


if __name__ == '__main__':
    play(Harry())
