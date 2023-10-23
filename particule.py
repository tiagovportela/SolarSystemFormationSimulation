# THE PARTICLE CLASS WILL HAVE THE FOLLOWING ATTRIBUTES:
# MASS, POSITION, VELOCITY, ACCELERATION
# Position is a vector, represented as a numpy array
# Velocity is a vector, represented as a numpy array
# Acceleration is a vector, represented as a numpy array
# Mass is a scalar, represented as a float

import numpy as np
import math

mass = 2.0
position = np.array([0.0, 0.0])
velocity = np.array([0.0, 0.0])
acceleration = np.array([0.0, 0.0])

class Particle:
    def __init__(self, mass, position, velocity, acceleration):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    def get_mass(self):
        return self.mass
    
    def get_position_x(self):
        return self.position[0]
    
    def get_position_y(self):
        return self.position[1]
    
    def get_velocity_x(self):
        return self.velocity[0]
    
    def get_velocity_y(self):
        return self.velocity[1]
    
    def get_acceleration_x(self):
        return self.acceleration[0]
    
    def get_acceleration_y(self):
        return self.acceleration[1]
    
    def set_mass(self, mass):
        self.mass = mass

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def update_position(self, dt):
        self.position = self.position + self.velocity * dt
    
    def update_velocity(self, dt):
        self.velocity = self.velocity + self.acceleration * dt

    def __str__(self):
        return "Mass: " + str(self.mass) + " Position: " + str(self.position) + " Velocity: " + str(self.velocity) + " Acceleration: " + str(self.acceleration)


# Using the particula class, i will create a system of particles
# The system will have the following attributes:
# Particles, Time, dt
# Particles is a list of particles
# Time is a scalar, represented as a float
# dt is a scalar, represented as a float



# Create a system of particles

class System:
    def __init__(self, particles, time, dt):
        self.particles = particles
        self.time = time
        self.dt = dt
        self.G = 6.67408e-11
    
    def get_particles(self):
        return self.particles
    
    def get_time(self):
        return self.time
    
    def get_dt(self):
        return self.dt
    
    def apply_force(self, force):
        for particle in self.particles:
            # the only force in this system is gravity, this is a N-Body system in vacum
            # F_x = G * m1 * m2 * (x2 - x1) / (r^3)
            # F_y = G * m1 * m2 * (y2 - y1) / (r^3)
            # r = sqrt((x2 - x1)^2 + (y2 - y1)^2)
            for other in self.particles:
                if particle != other:
                    r = math.sqrt((other.get_position_x() - particle.get_position_x())**2 + (other.get_position_y() - particle.get_position_y())**2)
                    force_x = self.G  * particle.get_mass() * other.get_mass() * (other.get_position_x() - particle.get_position_x()) / (r**3)
                    force_y = self.G  * particle.get_mass() * other.get_mass() * (other.get_position_y() - particle.get_position_y()) / (r**3)
                    force = np.array([force_x, force_y])
                    particle.set_acceleration(force / particle.get_mass())
                    particle.update_velocity(self.dt)
                    particle.update_position(self.dt)

#run the system and save the data to a dictionary

number_of_particles = 5
time = 0.0
dt = 0.1

# Create a list of particles
particles = []
for i in range(number_of_particles):
    mass = 1.0
    position = np.array([0.0, 0.0])
    velocity = np.array([0.0, 0.0])
    acceleration = np.array([0.0, 0.0])
    particle = Particle(mass, position, velocity, acceleration)
    particles.append(particle)

system = System(particles, time, dt)
data = {}

for i in range(100):
    system.apply_force(0)
    data[i] = system.get_particles()
    
