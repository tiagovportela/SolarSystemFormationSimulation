import numpy as np
class Physics:
    SOLAR_SYSTEM_RADIUS = 6.7e12 # meters
    SOLAR_SYSTEM_MASS = 1.989e30 # kg
    SOLAR_SYSTEM_TEMPERATURE = 5778 # K
    SOLAR_SYSTEM_AREA = 4 * np.pi * SOLAR_SYSTEM_RADIUS**2
    SOLAR_SYSTEM_DENSITY = SOLAR_SYSTEM_MASS/SOLAR_SYSTEM_AREA # mus of the mass is on a plane 
    G = 6.67408e-11 # m^3 kg^-1 s^-2
    Z = 0.1
    K = 1.38e-23 # Boltzmann constant (J/K)