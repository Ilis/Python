import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


m = np.linspace(0, 21, 300)
g = np.linspace(0, 11, 20)

print(m)
print(g)

mm, gg = np.meshgrid(g, m, sparse=True)

print(mm)
print(gg)


def zero(p1, p2):
    return p1*0 + p2*0


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


def tar2(m, g):
    base = 50
    p = base
    if m > 100:
        p += (m - 100) * 3
    if g <= 4:
        pass
    elif 4 < g <= 8:
        p += 150
    elif 8 < g <= 20:
        p += 300
    else:
        p += 450
    return p


def tar_flat(m, g):
    base = 0
    p = base
    if m >= 0:
        p += m * 2.5
    if g >= 0:
        p += g * 100
    return p


f1 = tar1
f2 = tar2

p1 = zero(mm, gg)
p2 = zero(mm, gg)

for mc in range(len(m)):
    for gc in range(len(g)):
        p1[mc][gc] = f1(mc, gc)
        p2[mc][gc] = f2(mc, gc)

print(p1)
print(p2)

ax = plt.axes(projection='3d')
ax.plot_surface(gg, mm, p1, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.plot_wireframe(gg, mm, p2, rstride=20, cstride=1, color='blue', linewidth=0.2)
ax.set_title('Тариф')
ax.set_xlabel('Минуты')
ax.set_ylabel('Гигабайты')
ax.set_zlabel('Руб')

plt.show()
