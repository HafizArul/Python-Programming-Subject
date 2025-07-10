import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung polinomial Lagrange
def lagrange_polynomial(x_points, y_points):
    # Variabel simbolik untuk persamaan
    x = sp.symbols('x')
    n = len(x_points)
    polynomial = 0

    for i in range(n):
        # Hitung Lagrange basis polynomial L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        # Tambahkan kontribusi dari setiap L_i(x)
        polynomial += L_i * y_points[i]

    # Sederhanakan persamaan
    polynomial = sp.simplify(polynomial)
    return polynomial

# Masukkan titik data
x_points = [1, 3, 6, 8, 11]  # Bulan (Januari=1, Maret=3, dst.)
y_points = [1.2, 2.9, 1.6, 2.2, 2.3]  # Laba penjualan (dalam jutaan)

# Hitung polinomial interpolasi
polynomial = lagrange_polynomial(x_points, y_points)

# Tampilkan hasil
print("Persamaan polinomial hasil interpolasi adalah:")
sp.pretty_print(polynomial)

# Hitung laba penjualan pada bulan Mei (x = 5)
x_val = 5
laba_mei = sp.N(polynomial.subs(sp.symbols('x'), x_val))
print(f"Laba penjualan pada bulan Mei adalah: {laba_mei:.2f} juta")

# Tampilkan grafik
x_symbol = sp.symbols('x')
f_lagrange = sp.lambdify(x_symbol, polynomial, modules=['numpy'])
x_vals = np.linspace(1, 11, 100)
y_vals = f_lagrange(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Polinomial Interpolasi', color='blue')
plt.scatter(x_points, y_points, color='red', label='Titik Data')
plt.axvline(x=x_val, color='green', linestyle='--', label=f'Bulan Mei (x={x_val})')
plt.scatter(x_val, laba_mei, color='purple', label=f'Laba Mei: {laba_mei:.2f} juta')
plt.title('Interpolasi Polinomial Lagrange')
plt.xlabel('Bulan')
plt.ylabel('Laba Penjualan (Jutaan)')
plt.legend()
plt.grid()
plt.show()
