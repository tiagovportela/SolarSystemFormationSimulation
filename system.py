import numpy as np
from particule import Particle
class System:
    def __init__(self, particles, time, dt):
        self.particles = particles
        self.time = time
        self.dt = dt
        self.G =  6.67408e-11 #1*10**-10
        self.collision_coeficion = 0.75
        self.particles_distance = {}
        self.data = {}
    def get_particles(self):
        return self.particles
    
    def get_time(self):
        return self.time
    
    def get_dt(self):
        return self.dt
    
    def apply_force(self):
        
        for particle in self.particles:
            # the only force in this system is gravity, this is a N-Body system in vacum
            # F_x = G * m1 * m2 * (x2 - x1) / (r^3)
            # F_y = G * m1 * m2 * (y2 - y1) / (r^3)
            # r = sqrt((x2 - x1)^2 + (y2 - y1)^2)
            force_x = 0.0
            force_y = 0.0
            for other in self.particles:
                if particle.get_name() == other.get_name():
                    
                    continue
                r = np.sqrt((other.get_position_x() - particle.get_position_x())**2 + (other.get_position_y() - particle.get_position_y())**2)
                if r < 0.1:
                    r = 0.1
                
                self.particles_distance["{}_{}".format(particle.get_name(), other.get_name())] = r

                force_x += self.G  * particle.get_mass() * other.get_mass() * (other.get_position_x() - particle.get_position_x()) / (r**3)
                force_y += self.G  * particle.get_mass() * other.get_mass() * (other.get_position_y() - particle.get_position_y()) / (r**3)
            force = np.array([force_x, force_y])
            particle.set_acceleration(force / particle.get_mass())
            particle.update_velocity_x(self.dt)
            particle.update_velocity_y(self.dt)
            particle.update_position_x(self.dt)
            particle.update_position_y(self.dt)
            if particle.get_name() not in self.data.keys():
                self.data[particle.get_name()] = {'x': [], 'y': [], 'time': []}
            self.data[particle.get_name()]['x'].append(particle.get_position_x())
            self.data[particle.get_name()]['y'].append(particle.get_position_y())
            self.data[particle.get_name()]['time'].append(self.get_time())
    
    def particle_collision(self):
        particles_to_remove = [] 
        for particle in self.particles:
            mass = particle.get_mass()
            position_x = particle.get_position_x()
            position_y = particle.get_position_y()
            velocity_x = particle.get_velocity_x()
            velocity_y = particle.get_velocity_y()
            acceleration_x = particle.get_acceleration_x()
            acceleration_y = particle.get_acceleration_y()
            radius = particle.get_radius()

            for other in self.particles:
                if particle.get_name() == other.get_name():
                    continue
                particle_par = "{}_{}".format(particle.get_name(), other.get_name())
                r = self.particles_distance.get(particle_par)
                if r is None:
                    continue
                d = np.sqrt((other.get_position_x() - particle.get_position_x())**2 + (other.get_position_y() - particle.get_position_y())**2)
                if d < (particle.get_radius() + other.get_radius()):
                #if r < (particle.get_radius() + other.get_radius()):
                    print("collision between {} and {}".format(particle.get_name(), other.get_name()))
                    mass = self.collision_coeficion*(mass + other.get_mass())
                    
                    position_x = (position_x + other.get_position_x()) / 2
                    position_y = (position_y + other.get_position_y()) / 2

                    velocity_x = (velocity_x+ other.get_velocity_x()) / 2
                    velocity_y = (velocity_y + other.get_velocity_y()) / 2
                    velocity = np.array([velocity_x, velocity_y])

                    acceleration_x = (acceleration_x + other.get_acceleration_x()) / 2
                    acceleration_y = (acceleration_y + other.get_acceleration_y()) / 2
                    acceleration = np.array([acceleration_x, acceleration_y])

                    radius = self.collision_coeficion * (radius + other.get_radius())

                    

                    self.particles.append(particle)
                    #articles_to_remove.append(other)
                    if particle not in particles_to_remove:
                        particles_to_remove.append(particle)
                    if other not in particles_to_remove:
                        particles_to_remove.append(other)   
                                   
        
        # Remove the particles after the loop
        for particle in particles_to_remove:
            self.particles.remove(particle)
        
        new_particle = Particle(mass, np.array([position_x, position_y]), velocity, acceleration, radius)
        self.particles.append(new_particle)

    def particle_collision_2(self):
        particles_to_remove = []
        new_particle = None
        for particle in self.particles:
            mass = particle.get_mass()
            position_x = particle.get_position_x()
            position_y = particle.get_position_y()
            velocity_x = particle.get_velocity_x()
            velocity_y = particle.get_velocity_y()
            acceleration_x = particle.get_acceleration_x()
            acceleration_y = particle.get_acceleration_y()
            radius = particle.get_radius()
            for other in self.particles:
                if particle.get_name() == other.get_name():
                    continue

                particle_par = "{}_{}".format(particle.get_name(), other.get_name())
                r = self.particles_distance.get(particle_par)

                if r is None:
                    continue

                if r < (particle.get_radius() + other.get_radius()):
                    print("collision between {} and {}".format(particle.get_name(), other.get_name()))

                    # Update properties for merging particles
                    mass = self.collision_coeficion*(mass + other.get_mass())
                    
                    position_x = (position_x + other.get_position_x()) / 2
                    position_y = (position_y + other.get_position_y()) / 2

                    velocity_x = (velocity_x + other.get_velocity_x()) / 2
                    velocity_y = (velocity_y + other.get_velocity_y()) / 2

                    acceleration_x = (acceleration_x + other.get_acceleration_x()) / 2
                    acceleration_y = (acceleration_y + other.get_acceleration_y()) / 2

                    radius = self.collision_coeficion * (radius + other.get_radius())

                    # Append both particles to the removal list
                    particles_to_remove.append(particle)
                    particles_to_remove.append(other)

                    # Create a new merged particle
                    new_particle = Particle(mass, np.array([position_x, position_y]), 
                                            np.array([velocity_x, velocity_y]), 
                                            np.array([acceleration_x, acceleration_y]), radius)

        # Remove the particles after the loop
        for particle in particles_to_remove:
            if particle in self.particles:
                self.particles.remove(particle)

        
        if new_particle is not None:
            self.particles.append(new_particle)