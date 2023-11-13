# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-20, 20, 1000)
# y = x * x
# plt.plot(x, y)
# plt.show()
#
# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.xlabel('Trục X')
# plt.ylabel('Trục Y')
# plt.title('Hàm Sin trong khoảng 0 đến 3pi')
# plt.legend(['SIN(x)'])
# plt.show()
#
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('Trục X')
# plt.ylabel('Trục Y')
# plt.title('Hàm SIN và COS trong khoảng 0 đến 3pi')
# plt.legend(['SIN(x)', 'COS(x)'])
# plt.show()
# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
#
# D = { 'CTTT': 60,
#     'Kế toán': 310,
#     'Kinh tế': 360,
#     'CNTT': 580,
#     'Cơ khí': 340,
#     'Thủy văn': 290 }
# plt.bar(range(len(D)), D.values(), align='center')
# plt.xticks(range(len(D)), D.keys())
# plt.title('Các ngành tuyển sinh của Đại học Thủy Lợi')
# plt.show()# Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
#
# D = { 'CTTT': 60,
#     'Kế toán': 310,
#     'Kinh tế': 360,
#     'CNTT': 580,
#     'Cơ khí': 340,
#     'Thủy văn': 290 }
# # Biểu đồ dạng cột chiều ngang
# plt.barh(range(len(D)), list(D.values()))
# plt.yticks(range(len(D)), D.keys())
# plt.title('Các ngành tuyển sinh của Đại học Thủy Lợi')
# plt.show()
#
# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Ghép hai biểu đồ
# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="One", color = 'r')
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Two", color='g')
# plt.legend()
# plt.xlabel('bar number')
# plt.ylabel('bar height')
# plt.title('Ghép 2 biểu đồ')
# plt.show()
#
#
# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# # Biểu đồ dạng bánh
# D = { 'CTTT': 60,
# 'Kế toán': 310,
# 'Kinh tế': 360,
# 'CNTT': 580,
# 'Cơ khí': 340,
# 'Thủy văn': 290 }
#
# plt.pie(D.values(), labels=D.keys(), autopct='%1.1f%%')
# plt.axis('equal') # trục x = trục y
# plt.show()
#
# # Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# # Chia thành các biểu đồ con
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.subplot(2, 1, 1) # biểu đồ 1
# plt.plot(x, y_sin)
# plt.title('SIN(x)')
# plt.subplot(2, 1, 2) # biểu đồ 2
# plt.plot(x, y_cos)
# plt.title('COS(x)')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
# Ví dụ với thư viện matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# # Chia thành các biểu đồ con
# x = np.arange(0, 3 * np.pi, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# y_sinpi = np.sin(x + np.pi/4)
# y_cospi = np.cos(x + np.pi/4)
#
# plt.subplot(2, 2, 1) # biểu đồ 1
# plt.plot(x, y_sin)
# plt.title('SIN(x)')
# plt.subplot(2, 2, 2) # biểu đồ 2
# plt.plot(x, y_cos)
# plt.title('COS(x)')
#  # Biểu đồ 3
# plt.subplot(2,2,3)
# plt.plot(x,y_sinpi)
# plt.title('SIN(x + π/4)')
#  # Biểu đồ 4
# plt.subplot(2,2,4)
# plt.plot(x,y_cospi)
# plt.title('COS(x + π/4)')
# plt.show()
# plt.savefig('1.png')

# Ví dụ tính đạo hàm
# from sympy import *
# x = symbols('x')
# f1 = -3*x**4 + 5*x**2 + 7*x + 8
# dao_ham1 = diff(f1, x)
# dao_ham2 = diff(dao_ham1, x)
# dao_ham3 = diff(dao_ham2, x)
# print(f"Hàm f1: {f1}")
# print(f"Đạo hàm bậc một hàm f1: f1' = {dao_ham1}")
# print(f"Đạo hàm bậc hai hàm f1: f1'' = {dao_ham2}")
# print(f"Đạo hàm bậc ba hàm f1: f1''' = {dao_ham3}")

# Vẽ đồ thị đạo hàm
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5, 5, 0.1)
y1 = -3*x**4 + 5*x**2 + 7*x + 8
y2 = -12*x**3 + 10*x + 7
y3 = 10 - 36*x**2
y4 = -72*x
fig, ax = plt.subplots()
ax.plot(x, y1, label='$y=-3x^4 + 5x^2 +7x + 8$')
ax.plot(x, y2, label='$đạo hàm bậc 1 y=-12x^3 + 10x + 7$')
ax.plot(x, y3, label='$đạo hàm bậc 2 y= 10 - 36x^2$')
ax.plot(x, y4, label='$đạo hàm bậc 3 y= -72x$')
ax.set_xlabel("Trục hoành - X")
ax.set_ylabel("Trục tung - Y")
ax.legend()
plt.show()