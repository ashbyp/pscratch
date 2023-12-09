from utils.measure import *


@timefunc('count_ones')
def count_ones_less_than(n):
    # count = 0
    # for x in range(n):
    #     count += sum([1 for s in str(x) if s == '1'])
    # return count

    return sum([1 for x in range(n) for y in str(x) if y == '1'])


if __name__ == '__main__':
    print(count_ones_less_than(12))