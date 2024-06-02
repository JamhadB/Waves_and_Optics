import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
dt = 0.01  # Time step (s)

# Initial conditions
v0 = 20.0  # Initial velocity (m/s)
theta = np.radians(45)  # Launch angle (radians)
x0 = 0.0  # Initial position in x-direction (m)
y0 = 0.0  # Initial position in y-direction (m)

# Function to calculate projectile motion
def projectile_motion(v0, theta):
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    t = 0.0
    x = x0
    y = y0
    while y >= 0:
        x = x0 + vx0 * t
        y = y0 + vy0 * t - 0.5 * g * t**2
        t += dt
        yield x, y

# Simulate projectile motion
trajectory = np.array(list(projectile_motion(v0, theta)))

# Plot trajectory
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.title('Projectile Motion')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()
