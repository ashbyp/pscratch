import numpy as np
import matplotlib.pyplot as plt
import scipy


def hist():
    data = np.random.normal(0, 1, 1000)
    _, bins, _ = plt.hist(data, 20, density=1, alpha=0.5)
    mu, sigma = scipy.stats.norm.fit(data)
    best_fit_line = scipy.stats.norm.pdf(bins, mu, sigma)
    plt.plot(bins, best_fit_line)
    plt.show()


def hist_sub():
    fig, axs = plt.subplots(2)
    axs[0].set_title('Test')
    data = [x for x in range(10000)]
    n, bins, patches = axs[0].hist(data, 20, density=1, alpha=0.5)
    mu, sigma = scipy.stats.norm.fit(data)
    best_fit_line = scipy.stats.norm.pdf(bins, mu, sigma)
    axs[0].plot(bins, best_fit_line, color='green', linestyle='dashed')
    axs[1].plot(bins, best_fit_line, color='green', linestyle='dashed')
    plt.show()


if __name__ == '__main__':
    hist()
    hist_sub()