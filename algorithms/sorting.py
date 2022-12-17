import copy
import random


def bubble(a: list[int]) -> list[int]:
    a = copy.copy(a)
    for i in range(len(a) - 1):
        swapped = False
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        if not swapped:
            break
    return a


def quick_sort(a):
    def partition(pa, low, high):
        pivot = pa[high]
        i = low - 1

        for j in range(low, high):
            if pa[j] <= pivot:
                i = i + 1
                (pa[i], pa[j]) = (pa[j], pa[i])

        (pa[i + 1], pa[high]) = (pa[high], pa[i + 1])
        return i + 1

    def quick(qa, low, high):
        if low < high:
            pi = partition(qa, low, high)

            quick(qa, low, pi - 1)
            quick(qa, pi + 1, high)
        return qa

    return quick(copy.copy(a), 0, len(a) - 1)


def main():
    funcs = (('bubble', bubble,), ('quick', quick_sort))
    lists = ([], [1], [1,2,3,4,5], [5,4,3,2,1], [3,2,5,4,1], random.sample(range(1, 100), 20))

    for name, func in funcs:
        print(name)
        print('===')
        for l in lists:
            print(f'{l} -> {func(l)}')


if __name__ == '__main__':
    main()