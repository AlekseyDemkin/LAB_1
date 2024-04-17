import matplotlib.pyplot as plt
import numpy as np


def Function(t):
    if -1.25 <= t < 1.25:
        return 4 + (3.2 * t) * 1j
    if 1.25 <= t < 3.75:
        return 8 - 3.2 * t + (4) * 1j
    if 3.75 <= t < 6.25:
        return -4 + (16 - 3.2 * t) * 1j
    if 6.25 <= t < 8.75:
        return -24 + 3.2 * t + (-4) * 1j


Function = np.vectorize(Function)


def fourier_coefficients(Function, N, T, t):
    coefficients = []
    for n in range(-N+1, N):
        c = 1 / T * np.trapz(Function(t) * np.exp(-1j * 2 * np.pi * n * t / T), t)
        coefficients.append(c)
    return coefficients



def fourier_sum(t, coefficients, T, N):
    series_sum = np.zeros_like(t, dtype=complex)
    for n in range(-N, N + 1, 1):
        series_sum += coefficients[n + N] * np.exp(1j * 2 * np.pi * n * t / T)
    return series_sum


def PersCheck(Cn, T, Function):
    t = np.linspace(-1.25, 8.7499, 1000)
    L = np.trapz(np.abs(Function(t))**2, t) / T
    R = (sum(abs(c) ** 2 for c in Cn))
    return L, R


T = 10
N = 1
t = np.linspace(-1.25, 8.7499, 1000)
C = fourier_coefficients(Function, N + 1, T,t)
print(C)
"""left, right = PersCheck(C, T, Function)
print(f"Левая сторона условия Персеваля (L): {left}")
print(f"Правая сторона условия Персеваля (R): {right}")"""
Mass = [Function(ti) for ti in t]
print(Mass)
Re, Im, ReC, ImC = [], [],[],[]
for i in Mass:
    Re.append(i.real)
    Im.append(i.imag)
for i in C:
    ReC.append(i.real)
    ImC.append(i.imag)
plt.plot(t, fourier_sum(t, C, T, N).real, label='Row Re', color='red')
plt.plot(t, Re, label='Function Re', color='blue')
plt.title('Gn of Сomplex function')
plt.xlabel('t')
plt.ylabel('Re')
plt.legend()
plt.grid(True)
plt.show()

