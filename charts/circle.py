import matplotlib.pyplot as plt
import numpy as np


def main():
    # numpy
    a = np.arange(0, 2 * np.pi, 0.1)
    x = 100 * np.cos(a)
    y = 100 * np.sin(a)
    plt.title('Circle', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20}, color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, label='small', color='green', linewidth=1, markersize=5, marker='.', linestyle='--')
    x *= 2
    y *= 2
    plt.plot(x, y, label='big', color='red', linewidth=1, markersize=5, marker='.')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
