import matplotlib.pyplot as plt
import numpy as np


with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    # http://xkcd.com/418/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xticks([])
    plt.yticks([])
    # ax.set_ylim([-30, 10])

    x = np.arange(-np.pi, +np.pi, 0.1)
    y = np.sin(x)
    # data = np.ones(100)
    # data[70:] -= np.arange(30)

    plt.annotate(
        'x ≈ y',
        xy=(0, 0), arrowprops=dict(arrowstyle='->'), xytext=(-1, 0.5))

    plt.plot(x, y)

    plt.xlabel('x')
    plt.ylabel('sin(x)')
    fig.text(
        0.5, 0.05,
        'XKCD Sin',
        ha='center')

plt.show()
