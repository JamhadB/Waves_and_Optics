%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L = 2*np.pi  # Length of the domain
k = 2.0  # Wavenumber
omega = 2.0  # Angular frequency

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(0, L, 1000)
line, = ax.plot(x, np.sin(k*x), lw=2)

# Initialization function
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

# Animation function which updates the plot
def animate(i):
    y = np.sin(k*x - omega*i/10.0)  # Update the data for the y-axis
    line.set_ydata(y)
    return line,

# Create the animation object
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
