import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def Function1(t, period):
    half_period = period / 2
    return 5 if int(t / half_period) % 2 == 0 else 7


def an(n, Function1, T):
    def integrand(t):
        return Function1(t, T) * np.cos(2 * np.pi * n * t / T)
    return quad(integrand, 0, T)[0] * 2 / T


def bn(n, Function1, T):
    def integrand(t):
        return Function1(t, T) * np.sin(2 * np.pi * n * t / T)
    return quad(integrand, 0, T)[0] * 2 / T


def f_fourier(t, N):
    SumR = a0
    for n in range(1, N + 1):
        SumR += an(n, Function1, T) * np.cos(2 * np.pi * n * t / T) + bn(n, Function1, T) * np.sin(2 * np.pi * n * t / T)
    return SumR


t = np.linspace(0, 10, 1000)
T = 60
N = 3

a0 = quad(Function1, 0, T, args=(T,))[0] / T
for n in range(0, N+1):
    a_n = an(n, Function1, T)
    b_n = bn(n, Function1, T)
    print(f"n = {n}: a_n = {a_n}, b_n = {b_n}")
Ft = [Function1(ti, T) for ti in t]
series_sum = f_fourier(t, N)
plt.plot(t, Ft, label='Function', color='blue')
plt.plot(t, series_sum, label='Row', color='red')
plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Fn of the function_4')
plt.grid(True)
plt.legend()
plt.show()

