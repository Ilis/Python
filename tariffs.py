import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


m = np.linspace(0, 300, 51)
g = np.linspace(0, 50, 41)


def tar1(m, g):
    base = 200
    p = base
    if m > 100:
        p += (m - 100) * 1.5
    if g <= 4:
        pass
    elif 4 < g <= 8:
        p += 100
    elif 8 < g <= 20:
        p += 200
    else:
        p += 300
    return p


p = np.zeros((len(m), len(g)))

f = tar1
for gc in range(len(g)):
    for mc in range(len(m)):
        p[mc][gc] = f(m[mc], g[gc])

gg, mm = np.meshgrid(g, m, sparse=True)

ax = plt.axes(projection='3d')
ax.plot_surface(mm, gg, p, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('Тариф')
ax.set_xlabel('Минуты')
ax.set_ylabel('Гигабайты')
ax.set_zlabel('Руб')

plt.show()
