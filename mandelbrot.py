import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return 0
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    mandelbrot_image = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            mandelbrot_image[i, j] = mandelbrot(complex(x[i], y[height - 1 - j]), max_iter)  # Reverse the order of y

    return mandelbrot_image

def plot_mandelbrot(mandelbrot_image, x_min, x_max, y_min, y_max):
    plt.imshow(mandelbrot_image, cmap='viridis', extent=(x_min, x_max, y_min, y_max)) 
    plt.xlim(-1.5, 1.5)  # Set x-axis limits
    plt.ylim(-1, 2)  # Set y-axis limits
    plt.axis('off')  # Turn off axis labels and ticks
    #plt.show()
    plt.savefig('mandelbrot_full.png', dpi = 1000)

if __name__ == "__main__":
    width, height = 4000, 4000
    # 3000,3000
    x_min, x_max = -2, 2  # Adjust the x-axis limits for zooming
    y_min, y_max = -2, 2   # Adjust the y-axis limits for zooming
    max_iter = 100

    mandelbrot_image = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    plot_mandelbrot(mandelbrot_image, x_min, x_max, y_min, y_max)
