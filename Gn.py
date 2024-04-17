import numpy as np
import matplotlib.pyplot as plt


def Function1(t, period):
    half_period = period / 2
    return 5 if int(t / half_period) % 2 == 0 else 7


Function1 = np.vectorize(Function1)


def fourier_coefficients(Function1, N, T):
    coefficients = []
    t = np.linspace(0, T, 1000)
    for n in range(-N+1, N):
        c = 1 / T * np.trapz(Function1(t, T) * np.exp(-1j * 2 * np.pi * n * t / T), t)
        coefficients.append(c)
    return coefficients


def fourier_sum(t, coefficients, T, N):
    series_sum = np.zeros_like(t, dtype=complex)
    for n in range(-N, N+1, 1):
        series_sum += coefficients[n + N] * np.exp(1j * 2 * np.pi * n * t / T)
    return series_sum


T = 60
N = 3
t_values = np.linspace(0, 10, 1000)
C = fourier_coefficients(Function1, N + 1, T)
for n in range(0, len(C)):
    c_n = C[n]
    print(f"n = {n}: c_n = {c_n}")
f_values = [Function1(t, T) for t in t_values]
plt.plot(t_values, f_values, label='Function', color='blue')
plt.plot(t_values, fourier_sum(t_values, C, T, N), label='Row', color='red')
plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Gn of the function_4')
plt.legend()
plt.grid(True)
plt.show()
