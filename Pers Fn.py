import numpy as np
from scipy.integrate import quad


def Function1(t, period):
    return (np.sin(t))**5+(np.cos(2*t))


Function1 = np.vectorize(Function1)


def an(n, Function1, T):
    def integrand(t):
        return Function1(t, T) * np.cos(2 * np.pi * n * t / T)

    return quad(integrand, 0, T)[0] * 2 / T


def bn(n, Function1, T):
    def integrand(t):
        return Function1(t, T) * np.sin(2 * np.pi * n * t / T)

    return quad(integrand, 0, T)[0] * 2 / T


def PersCheck(An, Bn, T, Function1):
    t = np.linspace(0, T, 1000)
    L = np.trapz(Function1(t, T) ** 2, t) / T
    R = (sum(a ** 2 for a in An) + sum(b ** 2 for b in Bn)) / 2
    return L, R


T = 2 * np.pi
N = 50
t = np.linspace(0, T, 1000)
An = [an(n, Function1, T) for n in range(N)]

Bn = [bn(n, Function1, T) for n in range(N)]
print(An)
print(Bn)
left, right = PersCheck(An, Bn, T, Function1)
print(f"Левая сторона условия Персеваля (L): {left}")
print(f"Правая сторона условия Персеваля (R): {right}")
