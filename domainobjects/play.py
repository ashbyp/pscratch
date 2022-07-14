from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    # must be before data attributes
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    job: str
    gender: str = 'female'

    def __post_init__(self):
        # self.sort_index = self.age
        # needed because class is frozen
        object.__setattr__(self, 'sort_index', self.age)


def main():
    p1 = Person('paul', 53, 'programmer', 'male')
    p2 = Person('vic', 48, 'bookkeeper')
    p3 = Person('vic', 48, 'bookkeeper')
    print(p1)
    print(p2)
    print(id(p2) == id(p3))
    print(p2 == p3)
    # p2.job = 'mother'  # frozen
    print(p2 == p3)
    print(p1 > p2)


if __name__ == '__main__':
    main()
