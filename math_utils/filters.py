
def integrate(actual, target):
    return (15 * actual + target)/ 16


def plot():
    from numpy import sin, cos
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.integrate as integrate
    import matplotlib.animation as animation

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
    ax.grid()


    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    plt.show()


if __name__ == '__main__':
    actual = 0
    target = 100
    for i in range(500):
        actual = integrate(actual, target)
        print(actual)

    plot()


