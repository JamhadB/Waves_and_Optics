from sympy import symbols, integrate, sin, pi, Piecewise, pprint

# Define symbols
x, L, H, n = symbols('x L H n', real=True, positive=True)

# Define the piecewise function for y(x, 0)
y_x_0 = Piecewise((16*H/L**2 * (L/2 - x), (x < L/2)), (0, True))

# Integrate the piecewise function with the sine term over the interval from 0 to L/2
A_n_expr = 2/L * integrate(y_x_0 * sin(n*pi*x/L), (x, 0, L/2))

# Print the result
pprint(A_n_expr, use_unicode=True)