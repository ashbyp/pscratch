import os


def double_list(inlist: list[float]) -> list[float]:
    return [i * 2 for i in inlist]


def get_greeting(name: str) -> str:
    return f'hello {name or os.getlogin()}'


def main() -> None:
    print(get_greeting('paul'))
    print(get_greeting(None))
    print(double_list([1, "str", 3]))

if __name__ == '__main__':
    main()