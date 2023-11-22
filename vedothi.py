import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa hàm số y = x^4 - 2x^2 - 3
def func(x):
    return x**4 - 2 * x**2 - 3

# Đạo hàm bậc 1 của hàm số y = x^4 - 2x^2 - 3
def der1_func(x):
    return 4 * x**3 - 4 * x

# Đạo hàm bậc 2 của hàm số y = x^4 - 2x^2 - 3
def der2_func(x):
    return 12 * x**2 - 4

# Đạo hàm bậc 3 của hàm số y = x^4 - 2x^2 - 3
def der3_func(x):
    return 24 * x

# Tạo dữ liệu x từ -10 đến 10
x = np.linspace(-10, 10, 1000)

# Tính giá trị y cho từng giá trị x
y = func(x)
y_der1 = der1_func(x)
y_der2 = der2_func(x)
y_der3 = der3_func(x)

# Vẽ đồ thị
plt.figure(figsize=(10, 8))

# Đồ thị hàm số y = x^4 - 2x^2 - 3
plt.subplot(221)
plt.plot(x, y, label='y = x^4 - 2x^2 - 3')
plt.title('Hàm số y = x^4 - 2x^2 - 3')
plt.legend()

# Đồ thị đạo hàm bậc 1
plt.subplot(222)
plt.plot(x, y_der1, label="y'")
plt.title("Đạo hàm bậc 1")
plt.legend()

# Đồ thị đạo hàm bậc 2
plt.subplot(223)
plt.plot(x, y_der2, label="y''")
plt.title("Đạo hàm bậc 2")
plt.legend()

# Đồ thị đạo hàm bậc 3
plt.subplot(224)
plt.plot(x, y_der3, label="y'''")
plt.title("Đạo hàm bậc 3")
plt.legend()

plt.tight_layout()
plt.show()
