import numpy as np


def solve_equation():
    coeff_matrix = np.array([[2, -5, 1], [4, 2, -2], [1, 1, -1]])
    constants = np.array([-5, 2, 0])

    solution = np.linalg.solve(coeff_matrix, constants)
    return solution


# Gọi hàm để giải hệ phương trình
result = solve_equation()
print("Kết quả của hệ phương trình:")
print("x =", result[0])
print("y =", result[1])
print("z =", result[2])
def calculate_limit():
    from sympy import symbols, limit, sqrt

    x = symbols('x')
    f = ((x**3 - 3*x**2)**(1/3)) + ((x**2 - 2*x)**(1/2))

    limit_value = limit(f, x, 5)
    return limit_value

# Gọi hàm để tính giới hạn
result = calculate_limit()
print("Giới hạn của hàm khi x tiến tới 5 là:", result)
def calculate_derivative():
    from sympy import symbols, diff

    x = symbols('x')
    f = (2*x - 1) / (x + 2)

    derivative = diff(f, x)
    return derivative

# Gọi hàm để tính đạo hàm
result = calculate_derivative()
print("Đạo hàm của hàm là:", result)
def calculate_derivative():
    from sympy import symbols, diff

    x = symbols('x')
    f = (2*x - 1) / (x + 2)

    derivative = diff(f, x)
    return derivative

# Gọi hàm để tính đạo hàm
result = calculate_derivative()
print("Đạo hàm của hàm là:", result)
def calculate_integral_with_limits():
    from sympy import symbols, integrate, tan, cos, pi

    x = symbols('x')
    f = (1 - x*tan(x)) / (x**2 * cos(x) + x)

    integral = integrate(f, (x, 0, 2*pi/3))
    return integral

# Gọi hàm để tính tích phân
result = calculate_integral_with_limits()
print("Tích phân của hàm từ 0 đến 2pi/3 là:", result)
