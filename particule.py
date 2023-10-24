import numpy as np
import math
import string
import random


class Particle:
    def __init__(self, mass, position, velocity, acceleration, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        # name is a string random generated with 5 characters
        self.name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    
    def get_name(self):
        return self.name

    def get_radius(self):
        return self.radius

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

    def update_position_x(self, dt):
        self.position[0] = self.position[0] + self.velocity[0] * dt
    
    def update_position_y(self, dt):
        self.position[1] = self.position[1] + self.velocity[1] * dt
    
    def update_velocity_x(self, dt):
        self.velocity[0] = self.velocity[0] + self.acceleration[0] * dt
    
    def update_velocity_y(self, dt):
        self.velocity[1] = self.velocity[1] + self.acceleration[1] * dt

    

    def __str__(self):
        return "Mass: " + str(self.mass) + " Position: " + str(self.position) + " Velocity: " + str(self.velocity) + " Acceleration: " + str(self.acceleration)