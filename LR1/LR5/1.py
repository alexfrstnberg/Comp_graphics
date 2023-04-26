import numpy as np
import matplotlib.pyplot as plt

# Функція для візуалізації алгебраїчної кривої
def plot_algebraic_curve(a, b, c, d):
    x = np.linspace(-10, 10, 1000)
    y = np.zeros_like(x)
    for i, xi in enumerate(x):
      aa = (-a * xi**2 - b * xi - d) / c
      y[i] = np.array(aa)
    plt.plot(x, y)
    plt.grid()
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.show()

# Задаємо алгебраїчну криву другого порядку
a, b, c, d = 1, 2, 3, 4

# Задаємо матрицю коефіцієнтів системи рівнянь
A = np.array([[2*a, b],
              [b, 2*c]])

# Задаємо вектор вільних членів
b = np.array([-d, -d])

# Зводимо матрицю до трикутної форми
for i in range(A.shape[0]):
    # Ділення поточного рядка на діагональний елемент
    div = A[i, i]
    A[i, :] = A[i, :] / div
    b[i] /= div

    # Віднімання поточного рядка від інших рядків
    for j in range(i + 1, A.shape[0]):
        mult = A[j, i]
        A[j, :] -= mult * A[i, :]
        b[j] -= mult * b[i]

# Зворотній хід для знаходження розв'язку
x = np.zeros(A.shape[0])
for i in range(A.shape[0] - 1, -1, -1):
    x[i] = b[i]
    for j in range(i + 1, A.shape[0]):
        x[i] -= A[i, j] * x[j]

# Виводимо розв'язок системи
print("Розв'язок системи рівнянь:")
print('x =', x[0])
print('y =', x[1])

plot_algebraic_curve(a, b, c, d)
