import numpy as np
import matplotlib.pyplot as plt

# Lagrange Interpolation
def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result

# Input data
arr_x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
arr_y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# The x value for which y needs to be interpolated
x_val = 38.5  

# Compute the interpolated value at x_val
y_val = lagrange_interpolation(arr_x, arr_y, x_val)
print(f"Hasilnya adalah: {y_val}")

# Plotting the results
x_vals = np.linspace(min(arr_x), max(arr_x), 100)
y_vals = [lagrange_interpolation(arr_x, arr_y, x) for x in x_vals]

plt.plot(arr_x, arr_y, 'o', label='Data points')
plt.plot(x_vals, y_vals, label='Lagrange interpolation')
plt.axvline(x_val, color='r', linestyle='--', label=f'Interpolated x = {x_val}')
plt.axhline(y_val, color='g', linestyle='--', label=f'Interpolated y = {y_val:.8f}')
plt.legend()
plt.xlabel('Tegangan, x (Kg/mm^2)')
plt.ylabel('Waktu patahan, y (jam)')
plt.title('Lagrange Interpolation')
plt.grid(True)
plt.show()
