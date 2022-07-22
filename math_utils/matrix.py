from typing import Callable

import numpy as np
import copy

PythonMatrix = list[list[int | float | None]]
PythonVector = list[int | float | None]


def init(rows: int, cols: int, value: int | float | None = None) -> PythonMatrix:
    return [[value for _ in range(cols)] for _ in range(rows)]


def print_result(a: PythonMatrix | int | float) -> None:
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


def dot(a: PythonMatrix, b: PythonMatrix) -> PythonMatrix:
    c = init(len(a), len(b[0]), 0)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c


def multiply(a: PythonMatrix, b: PythonMatrix) -> PythonMatrix:
    c = init(len(a), len(a[0]), None)
    for row in range(len(a)):
        for col in range(len(a[0])):
            c[row][col] = a[row][col] * b[row][col]
    return c


def transpose(a: PythonMatrix) -> PythonMatrix:
    t = init(len(a[0]), len(a))

    for row in range(len(a)):
        for col in range(len(a[0])):
            t[col][row] = a[row][col]
    return t


def inner(a: PythonVector, b: PythonVector) -> int | float:
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def trace(a: PythonMatrix) -> int | float:
    res = 0
    for i in range(min(len(a), len(a[0]))):
        res += a[i][i]
    return res


def det(a: PythonMatrix) -> int | float:
    # store indices in list for row referencing
    indices = list(range(len(a)))

    # when at 2x2 sub-matrices recursive calls end
    if len(a) == 2 and len(a[0]) == 2:
        val = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return val

    total = 0
    # define sub-matrix for focus column and
    # call this function
    for fc in indices:  # A) for each focus column, ...
        # find the sub-matrix ...
        a_s = copy.copy(a)  # B) make a copy, and ...
        a_s = a_s[1:]  # ... C) remove the first row
        height = len(a_s)  # D)

        for i in range(height):
            # E) for each remaining row of sub-matrix ...
            #     remove the focus column elements
            a_s[i] = a_s[i][0:fc] + a_s[i][fc + 1:]

        sign = (-1) ** (fc % 2)  # F)
        # G) pass sub-matrix recursively
        sub_det = det(a_s)
        # H) total all returns from recursion
        total += sign * a[0][fc] * sub_det

    return total


def matrix_minor(a: PythonMatrix, i: int, j: int) -> PythonMatrix:
    return [row[:j] + row[j+1:] for row in (a[:i] + a[i+1:])]


def inv(a: PythonMatrix) -> PythonMatrix:
    determinant = det(a)
    if len(a) == 2:
        return [[a[1][1] / determinant, -1 * a[0][1] / determinant],
                [-1 * a[1][0] / determinant, a[0][0] / determinant]]
    cfs = []
    for r in range(len(a)):
        cf_row = []
        for c in range(len(a)):
            minor = matrix_minor(a, r, c)
            cf_row.append(((-1) ** (r + c)) * det(minor))
        cfs.append(cf_row)
    cfs = transpose(cfs)
    for r in range(len(cfs)):
        for c in range(len(cfs)):
            cfs[r][c] = cfs[r][c] / determinant
    return cfs


def compare(name: str, numpy_func: Callable, python_func: Callable, args: tuple) -> None:
    print(f'{name} =====================')
    numpy_result = numpy_func(*(np.array(a) for a in args))
    python_result = python_func(*args)
    print('Numpy:')
    print(numpy_result)
    print('Python:')
    print_result(python_result)
    print(f'Match = {np.allclose(numpy_result, python_result)}\n')


def eigvals(a: PythonMatrix) -> PythonMatrix:
    return a


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

    a = [[2, 2, 1, 10], [1, 3, 1, 122], [1, 2, 2, 10], [1, 1, 11, 111]]
    compare('DET', np.linalg.det, det, args=(a,))

    a = [[2, 2, 1, 10], [1, 3, 1, 122], [1, 2, 2, 10], [1, 1, 11, 111]]
    compare('INV', np.linalg.inv, inv, args=(a,))


if __name__ == '__main__':
    main()
