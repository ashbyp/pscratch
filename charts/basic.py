import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from utils.iters import float_range


def basic():
    # numpy
    x = np.arange(0, 360, 10)
    y = np.sin(np.radians(x))

    # python
    x1 = list(float_range(0, 360, 10))
    y1 = [math.cos(math.radians(i)) for i in x1]

    plt.figure(figsize=(7,4), dpi=100)
    plt.title('Sine/Cosine waves', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20}, color='blue')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xticks(np.arange(0, 361, 30))

    plt.annotate('90 degrees', (90, 1.0))

    plt.plot(x, y, label='Sin(x)', color='green', linewidth=2, markersize=5, marker='.', linestyle='--')
    plt.plot(x1, y1, label='Cos(x)', color='red', linewidth=2, markersize=5, marker='.', linestyle='--')
    plt.legend()
    plt.savefig('basic.png')


def bar():
    plt.figure(figsize=(6, 4))
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]
    bars = plt.bar(labels, values)
    bars[0].set_hatch('/')
    bars[1].set_hatch('.')
    bars[2].set_hatch('\\')
    plt.legend()


def main():
    basic()
    bar()
    plt.show()


if __name__ == '__main__':
    main()
