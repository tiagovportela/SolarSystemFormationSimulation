import numpy as np

from system import constants

def maxwell_boltzmann_velocity(mass, temperature):
    



    r1 = np.random.rand()  # Random number between 0 and 1
    r2 = np.random.rand()

    v = np.sqrt(-2 * constants.Physics.K * temperature / mass * np.log(1 - r1))
    v *= 1 if r2 > 0.5 else -1  # Random sign

    return v

def radius(mass):
    return (3*mass)/(constants.Physics.SOLAR_SYSTEM_DENSITY*4*np.pi) 