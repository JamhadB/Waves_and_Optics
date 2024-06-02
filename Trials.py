import sympy as sp

# Constants
P = 2.5  # power in Watts
I0 = 1e-12  # reference intensity in W/m^2
SIL_80dB = 80  # sound intensity level in dB

# Calculate the intensity corresponding to 80 dB
I_80dB = I0 * 10**(SIL_80dB/10)

# Symbol for r (distance from the source)
r = sp.symbols('r', real=True, positive=True)

# Equation for intensity I at distance r from the source (isotropic emission)
I_r = P / (4 * sp.pi * r**2)

# Solve for the distance r where the intensity I equals the intensity for 80 dB
r_80dB = sp.solve(I_r - I_80dB, r)

# Solve for part (b)
# If the intensity is 25 times smaller than the intensity for 80 dB, then
I_25_times_smaller = I_80dB / 25
r_25_times_smaller = sp.solve(I_r - I_25_times_smaller, r)

# Calculate the SIL for the intensity 25 times smaller
SIL_25_times_smaller = 10 * sp.log(I_25_times_smaller / I0, 10)

# Solve for part (c)
# The ratio of the amplitudes of the pressure oscillations is the square root of the ratio of intensities
amplitude_ratio = sp.sqrt(I_80dB / I_25_times_smaller)

print(r_80dB, r_25_times_smaller, SIL_25_times_smaller.evalf(), amplitude_ratio.evalf())

