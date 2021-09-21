
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from PIL import Image, GifImagePlugin
import time

def generar_animacion(nx, ny, valores_x, valores_y):
    x_data = []
    y_data = []

    fig, ax = plt.subplots()
    fig.set_size_inches(15, 7)
    ax.set_xlim(min(valores_x), max(valores_x))
    ax.set_ylim(min(valores_y), max(valores_y)+5000)
    plt.xlabel(nx)
    plt.ylabel(ny)
    line, = ax.plot(0,0)
    plt.title('DATOS OBTENIDOS POR EL MODELO LINEAL',fontsize=15)
    def init():
    	# creating an empty plot/frame
    	line.set_data([], [])
    	return line,

    def animation_frame(i):
        x_data.append(i+min(valores_x)-1)
        y_data.append(valores_y[int(i-1)])
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        return line,

        

    animation = FuncAnimation(fig, func=animation_frame, init_func=init, frames=np.arange(1, len(valores_x)+1, 1), interval = 0.05, repeat = False)
    animation.save('fig.gif', writer=PillowWriter(fps=5))
    plt.show()
