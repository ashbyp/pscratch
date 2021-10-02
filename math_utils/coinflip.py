import random


def flip(flips):
    x = [random.randint(0, 1) for _ in range(flips)]
    return sum(x)


if __name__ == '__main__':
    tries = 100000
    total = 0

    for _ in range(tries):
        if flip(3) > 1:
            total += 1
    print(total/tries)
