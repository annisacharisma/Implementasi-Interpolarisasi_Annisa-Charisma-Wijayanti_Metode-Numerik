import numpy as np
import matplotlib.pyplot as plt

# Newton Interpolation
def newton_interpolation(x, y, x_val):
    n = len(y)
    # Create a divided difference table
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    # Evaluate the interpolation polynomial at x_val
    result = coef[0, 0]
    product_term = 1
    for i in range(1, n):
        product_term *= (x_val - x[i - 1])
        result += coef[0, i] * product_term

    return result

# input data
arr_x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
arr_y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# The x value for which y needs to be interpolated
x_val = 12  

# Compute the interpolated value at x_val
y_val = newton_interpolation(arr_x, arr_y, x_val)
print(f"Hasilnya adalah: {y_val}")

# Plotting the results
x_vals = np.linspace(min(arr_x), max(arr_x), 100)
y_vals = [newton_interpolation(arr_x, arr_y, x) for x in x_vals]

plt.plot(arr_x, arr_y, 'o', label='Data points')
plt.plot(x_vals, y_vals, label='Newton interpolation')
plt.axvline(x_val, color='r', linestyle='--', label=f'Interpolated x = {x_val}')
plt.axhline(y_val, color='g', linestyle='--', label=f'Interpolated y = {y_val:.2f}')
plt.legend()
plt.xlabel('Tegangan, x (Kg/mm^2)')
plt.ylabel('Waktu patahan, y (jam)')
plt.title('Newton Interpolation')
plt.grid(True)
plt.show()
