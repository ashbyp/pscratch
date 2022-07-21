import numpy as np
import copy


def init(rows: int, cols: int, value: int | float | None = None):
    return [[value for _ in range(cols)] for _ in range(rows)]


def printm(a: list[list] | int | float) -> None:
    if isinstance(a, list):
        print('[', end='')
        for row in range(len(a)):
            if row:
                print(' ', end='')
            print('[', end='')
            for col in range(len(a[0])):
                if col:
                    print(' ', end='')
                print(a[row][col], end='')
            print(']', end='')
            if row != len(a) - 1:
                print('')
        print(']')
    else:
        print(a)


def dot(a: list[list], b: list[list]) -> list[list]:
    c = init(len(a), len(b[0]), 0)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


def multiply(a: list[list], b: list[list]) -> list[list]:
    c = init(len(a), len(a[0]), None)
    for row in range(len(a)):
        for col in range(len(a[0])):
            c[row][col] = a[row][col] * b[row][col]
    return c


def transpose(a: list[list]) -> list[list]:
    t = init(len(a[0]), len(a))

    for row in range(len(a)):
        for col in range(len(a[0])):
            t[col][row] = a[row][col]
    return t


def inner(a: list, b: list) -> int | float:
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def trace(a: list[list]) -> int | float:
    res = 0
    for i in range(min(len(a), len(a[0]))):
            res += a[i][i]
    return res


def det(A: list[list]) -> int | float:
    # store indices in list for row referencing
    indices = list(range(len(A)))

    # when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    total = 0
    # define submatrix for focus column and
    # call this function
    for fc in indices:  # A) for each focus column, ...
        # find the submatrix ...
        As = copy.copy(A)  # B) make a copy, and ...
        As = As[1:]  # ... C) remove the first row
        height = len(As)  # D)

        for i in range(height):
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = det(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det

    return total


def compare(name, npfunc, pyfunc, args):
    print(f'{name} =====================')
    nres = npfunc(*(np.array(a) for a in args))
    pres = pyfunc(*args)
    print('Numpy:')
    print(nres)
    print('Python:')
    printm(pres)
    print(f'Match = {np.array_equal(nres, pres)}\n')


def main() -> None:
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10], [11, 12]]
    compare('DOT', np.dot, dot, args=(a, b))

    a = [1, 2, 3]
    b = [4, 5, 6]
    compare('INNER', np.inner, inner, args=(a, b))

    a = [[1, 2], [4, 5]]
    b = [[7, 8], [9, 10]]
    compare('MULTIPLY', np.multiply, multiply, args=(a, b))

    a = [[1, 2, 3], [4, 5, 6]]
    compare('TRANSPOSE', np.transpose, transpose, args=(a,))

    a = [[1, 2], [4, 5]]
    compare('TRACE', np.trace, trace, args=(a,))

    a = [[1, 2, 3], [4, 5, 6]]
    compare('TRACE', np.trace, trace, args=(a,))

    a = [[1, 2], [3, 4], [5, 6]]
    compare('TRACE', np.trace, trace, args=(a,))

    a = [[2, 2, 1, 10], [1, 3, 1, 122], [1, 2, 2, 10], [1,1, 11,111]]
    compare('DET', np.linalg.det, det, args=(a,))


if __name__ == '__main__':
    main()
