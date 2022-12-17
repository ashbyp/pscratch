from scipy import constants
from scipy.optimize import root
from math import cos
from scipy.optimize import minimize
import numpy as np
from scipy.sparse import csr_matrix


def p_constants():
    print(constants.liter)
    print(dir(constants))


def root_find():
    def eqn(x):
        a = x + cos(x)
        print(a)
        return a

    myroot = root(eqn, 0)

    print(myroot.x)


def mini():
    def eqn(x):
        return x ** 2 + x + 2

    mymin = minimize(eqn, 0, method='BFGS')

    print(mymin)


def sparse():
    arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
    print(csr_matrix(arr))


def main():
    #p_constants()
    #root_find()
    #mini()
    sparse()


if __name__ == '__main__':
    main()