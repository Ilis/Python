import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 50)
y1 = np.cos(x) - 1
y2 = 2 * np.sin(x / 3.0)
y3 = x*x / 20.0 - 2
plt.plot(x, y1, c='c')
plt.plot(x, y2, c='m')
plt.plot(x, y3, c='y')

# print(type(y1), "\n", y1)

plt.show()
