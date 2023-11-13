import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_horse_saddle():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z = (x/3)**2 - (y/2)**2

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title('Horse Saddle Surface')
    plt.show()

def draw_hyperbolic_surface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z = np.sqrt((x/3)**2 + (y/5)**2 + 1)

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title('Hyperbolic Surface')
    plt.show()

def draw_sphere_surface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    x = 2 * np.sin(phi) * np.cos(theta) - 2
    y = 2 * np.sin(phi) * np.sin(theta) + 1
    z = 2 * np.cos(phi) + 4

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title('Sphere Surface')
    plt.show()

if __name__ == "__main__":
    while True:
        option = input("Enter an option (1 for horse saddle, 2 for hyperbolic surface, 3 for sphere surface, or 'q' to quit): ")

        if option == "1":
            draw_horse_saddle()
        elif option == "2":
            draw_hyperbolic_surface()
        elif option == "3":
            draw_sphere_surface()
        elif option.lower() == 'q':
            print("Exiting the program.")
            break  # Exit the loop if the user enters 'q'
        else:
            print("Invalid option. Please enter a valid option.")