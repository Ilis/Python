import numpy as np


m = np.linspace(0, 9, 10)
g = np.linspace(0, 5, 6)

print(m)
print(g)

mm, gg = np.meshgrid(g, m, sparse=True)

print(mm)
print(gg)
