import numpy as np
import matplotlib.pyplot as plt

A = 0.066
omega0 = 7.54
phi = 3.75

def x(t):
    x = A*np.cos(omega0*t + phi)
    return x

print(f"x(2) = {x(2):.4f}")

t = np.linspace(0, 5, 200)

plt.figure()
plt.plot(t, x(t))
plt.axhline(y=0, color = 'black', linestyle="--")
plt.axvline(x = 0.34 , color = 'purple', linestyle = '--')
plt.title("SHO with specified initial conditions")
plt.xlabel("t (in s)", fontsize = 14)
plt.ylabel("x(t) (in m)", fontsize = 14)
plt.show()