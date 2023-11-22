import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_horse_saddle():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = (x/3)**2 - (y/2)**2

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Mặt yên ngựa: z = (x/3)^2 - (y/2)^2')

    plt.show()

def plot_hyperboloid():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sqrt((x/3)**2 + (y/5)**2 + 1)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='plasma')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Mặt hyperbolic 1 tầng: (x/3)^2 + (y/5)^2 - (z/2)^2 = 1')

    plt.show()

def plot_sphere():
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 2 * np.outer(np.cos(u), np.sin(v)) - 2
    y = 2 * np.outer(np.sin(u), np.sin(v)) + 1
    z = 2 * np.outer(np.ones(np.size(u)), np.cos(v)) + 4

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, color='skyblue')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('Mặt cầu: (x + 2)^2 + (y - 1)^2 + (z - 4)^2 = 4')

    plt.show()

# Vẽ đồ thị cho mỗi loại mặt phẳng
plot_horse_saddle()
plot_hyperboloid()
plot_sphere()
