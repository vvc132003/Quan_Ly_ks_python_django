import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
def do_thi_yen_ngua(x, y):
    x, y = np.meshgrid(x, y)
    z = x**2 - 2*y**2
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})
    rosen_surf = ax.plot_surface(x, y, z,cmap=cm.coolwarm,
                                 linewidth=0, antialiased=False)
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    plt.show()
def main():
    x = np.linspace(start=-30,stop=30,num=200)
    y = np.linspace(start=-30, stop=30,num=200)
    do_thi_yen_ngua(x, y)
if __name__ == '__main__':
    main()