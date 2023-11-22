import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
x = np.linspace(-10, 10, num=2000)
y = np.linspace(-10, 10, num=2000)
x, y = np.meshgrid(x, y)
z1 =  (3*x**2 + 5*y**2)**(1/2)
z2 = -(3*x**2 + 5*y**2)**(1/2)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
rosen_surf1 = ax.plot_surface(x, y, z1, cmap=cm.coolwarm,
linewidth=0, antialiased=False)
rosen_surf2 = ax.plot_surface(x, y, z2, cmap=cm.coolwarm,
linewidth=0, antialiased=False)
fig.colorbar(rosen_surf1, shrink=0.5, aspect=5)
fig.colorbar(rosen_surf2, shrink=0.5, aspect=5)
plt.show()