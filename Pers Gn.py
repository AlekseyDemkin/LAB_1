import numpy as np



def Function1(t, period):
    return (np.sin(t))**5+(np.cos(2*t))


Function1 = np.vectorize(Function1)


def fourier_coefficients(Function1, N, T):
    coefficients = []
    t = np.linspace(0, T, 1000)
    for n in range(-N + 1, N):
        c = 1 / T * np.trapz(Function1(t, T) * np.exp(-1j * 2 * np.pi * n * t / T), t)
        coefficients.append(c)
    return coefficients


def PersCheck(Cn, T, Function1):
    t = np.linspace(0, T, 1000)
    L = np.trapz(Function1(t, T) ** 2, t) / T
    print(Function1(t, T) ** 2)
    R = (sum(abs(c) ** 2 for c in Cn))
    return L, R


T = 2 * np.pi
N = 50
t_values = np.linspace(0, T, 1000)
C = fourier_coefficients(Function1, N + 1, T)
left, right = PersCheck(C, T, Function1)
print(f"Левая сторона условия Персеваля (L): {left}")
print(f"Правая сторона условия Персеваля (R): {right}")

