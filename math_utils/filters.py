
def integrate(actual, target):
    return (15 * actual + target)/ 16


if __name__ == '__main__':
    actual = 0
    target = 100
    for i in range(500):
        actual = integrate(actual, target)
        print(actual)


