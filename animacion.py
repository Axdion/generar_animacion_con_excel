import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


x_data = []
y_data = []



fig, ax = plt.subplots()
ax.set_xlim(1990, 2025)
ax.set_ylim(0, 35000)
plt.xlabel('Años')
plt.ylabel('Producción de Gas en Metros Cúbicos')
line, = ax.plot(0, 0)

def animation_frame(i):
    x_data.append(i+1989)
    y_data.append((38.7*(i**2))-(180*i)+2772.7)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    print(f'{i+1989} {(38.7*(i**2))-(180*i)+2772.7}')


    return line,

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(1, 31, 0.1), interval = 1,  blit = False, repeat = False)
plt.show()
