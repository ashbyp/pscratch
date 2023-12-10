from pydantic import BaseModel

# class User(BaseModel):
class User:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    FRED:str="hello"

    def __str__(self):
        return self.name + " " + str(self.age) + " " + User.name


def main():
    u1 = User(name='paul', age=54)
    u2 = User(name='victoria', age=49)

    print(u1)
    print(u2)


if __name__ == '__main__':
    main()