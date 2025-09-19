def main(x: int):
    if x == 1: return 1
    if x == 2: return 1
    return main(x - 2) + main(x - 1)


if __name__ == '__main__':
    print(main(6)) # 1 1 2 3 5 8
