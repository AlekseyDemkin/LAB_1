import matplotlib.pyplot as plt
import numpy as np


def Function(t):
    if -1.25 <= t < 1.25:
        return 4, 3.2 * t
    if 1.25 <= t < 3.75:
        return 8 - 3.2 * t, 4
    if 3.75 <= t < 6.25:
        return -4, 16 - 3.2 * t
    if 6.25 <= t < 8.75:
        return -24 + 3.2 * t, -4
    else:
        pass


t = np.linspace(-1.25, 8.7499, 1000)
Mass = [Function(ti) for ti in t]
Re, Im = [], []
for i in Mass:
    Re.append(i[0])
    Im.append(i[1])
plt.scatter(Re, Im, s = 2)
plt.title('Сomplex function')
plt.xlabel('Re')
plt.ylabel('Im')
plt.grid(True)
plt.show()
