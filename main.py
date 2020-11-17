import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a = np.genfromtxt('start.dat.txt')
A = np.eye(50)
A[np.arange(50), np.arange(50)-1] = -1
fig, ax = plt.subplots()
x = np.arange(50)
line, = ax.plot(x, a)


def animate(i):
    global y
    if i == 0:
        y = a
    line.set_data(x, y)
    y = y - 0.5 * (A @ y)
    return line,


anim = animation.FuncAnimation(fig, animate, frames=255, interval=80, blit=True)
plt.show()
