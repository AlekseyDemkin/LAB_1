import matplotlib.pyplot as plt
import numpy as np


def Function1(t, period):
    half_period = period / 2
    return 5 if int(t / half_period) % 2 == 0 else 7


def Function2(t):
    return (np.cos(t))**6


def Function3(t):
    return (np.sin(t))**5


def Function4(t):
    return np.sin(t)**5 + np.cos(2*t)


t = np.linspace(0, 300, 1000)
period = 2*np.pi
Ft = [Function1(ti,60) for ti in t]
print(Ft)

plt.plot(t, Ft)
plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Graph of the function_1')
plt.grid(True)
plt.show()
