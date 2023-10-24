import pygame
import math
import pandas as pd
import numpy as np
import random
import time as time_lib

from particule import Particle
from system import System

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 2200, 1000
BACKGROUND_COLOR = (0,0,0)#(255, 255, 255)
PARTICLE_COLOR = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (128, 0, 0),    # Maroon
    (0, 128, 0),    # Green (dim)
    (0, 0, 128),    # Navy
    (128, 128, 0),  # Olive
    (0, 128, 128),  # Teal
    (128, 0, 128),  # Purple
    (255, 128, 0),  # Orange
    (255, 0, 128),  # Pink
    (128, 255, 0),  # Lime
    (0, 128, 255),  # Sky Blue
    (128, 0, 255),  # Lavender
    (128, 128, 128),  # Gray
    (192, 192, 192),  # Silver
    (128, 128, 128),  # Gray (dim)
    (255, 128, 128),  # Light Red
    (128, 255, 128),  # Light Green
    (128, 128, 255),  # Light Blue
    (255, 255, 128),  # Light Yellow
    (128, 255, 255),  # Light Cyan
    (255, 128, 255),  # Light Magenta
    (192, 0, 0),    # Dark Red
    (0, 192, 0),    # Dark Green
    (0, 0, 192),    # Dark Blue
    (192, 192, 0),  # Dark Yellow
    (0, 192, 192),  # Dark Cyan
    (192, 0, 192),  # Dark Magenta
    (64, 0, 0),     # Brown
    (64, 64, 0),    # Olive (dim)
    (0, 64, 0),     # Green (dark)
    (0, 0, 64),     # Navy (dark)
    (64, 0, 64),    # Purple (dark)
    (255, 192, 128),  # Peach
    (192, 255, 128),  # Lime (light)
    (128, 192, 255),  # Light Blue (light)
    (255, 128, 192),  # Pink (light)
    (192, 128, 255),  # Lavender (light)
    (128, 192, 128),  # Mint
    (128, 64, 0),     # Brown (dark)
    (0, 128, 64),     # Olive (dark)
    (64, 0, 128),     # Purple (dim)
    (128, 64, 64),    # Rosy Brown
]

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# Font
font = pygame.font.Font(None, 20)

# Create the pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-body Simulation")

# Main loop
running = True
clock = pygame.time.Clock()

df = pd.read_csv("./data/sol_data.csv")
df['distance'] = 0.5*df['perihelion'] + 0.5*df['aphelion'] 
df = df.sort_values(by=["distance"], ascending=True).reset_index(drop=True)

distances = df[(df.isPlanet == True)]["distance"].to_list()
masses = df[(df.isPlanet == True)]["mass_kg"].to_list()
radius = df[(df.isPlanet == True)]["meanRadius"].to_list()

distances.insert(0, 0)
masses.insert(0, 1.989*10**30)
radius.insert(0, 696340)



#masses = []
N = 20
particules_distribution = {}
for distance, mass in zip(distances, masses):
    particules_distribution[distance] = mass/N
    particules_distribution[distance] = mass/N
    particules_distribution[distance] = mass/N

paricules_positions = []
for distance, rd in zip(particules_distribution.keys(), radius):
    # sample from a normal distribution
    position = np.random.normal(distance, 2*distance, N)
    angles = np.random.uniform(0, 2 * np.pi, N)
    for d, a in zip(position, angles):
        mass = particules_distribution[distance]
        paricules_positions.append([d * np.cos(a), d * np.sin(a), mass, rd])

def convert_to_canvas_units(x, y):
    min_distance_in_pixel = 160
    filtered_distances= [x for x in distances if x > 0]
    scaling_factor = min_distance_in_pixel / (min(filtered_distances) * 10e2 )

    #return x*WIDTH/D, y*HEIGHT/D
    return x*scaling_factor, y*scaling_factor

time = 0.0
dt = 100.0

particles = []
w = 2*np.pi / 50 #365.25
for pos in paricules_positions:
    mass = pos[2]
    
    vel_x = w * pos[0]
    vel_y = - w * pos[1]

    velocity = np.array([vel_x, vel_y])
    acceleration = np.array([0.0, 0.0])
    position = np.array([pos[0], pos[1]])

    rd = pos[3]

    particle = Particle(mass, position, velocity, acceleration, rd)
    particles.append(particle)

# particles_random = []
# number_of_particles = 250

# def sample_solar_system_position():
#     # Standard deviation for the solar system size (rough estimate)
#     std_dev = 1e12  # 1 trillion meters

#     # Generate random positions from a Gaussian distribution
#     x = np.random.normal(0, std_dev)
#     y = np.random.normal(0, std_dev)

#     return np.array([x, y])

# position_list = []

# for i in range(number_of_particles):
#     mass = 10#1.989*10**30 / number_of_particles
    
#     position = sample_solar_system_position()

#     position_list.append(position[0])

#     vel_x = 0 #w * position[0]
#     vel_y = 0 #-w * position[1]

#     velocity = np.array([vel_x, vel_y])
#     acceleration = np.array([0.0, 0.0])
#     particle = Particle(mass, position, velocity, acceleration)
#     particles_random.append(particle)



# system = System(particles_random, time, dt)
system = System(particles, time, dt)


PARTICLE_COLOR = [random_color() for i in range(len(system.particles))]
text = ""
input_rect = pygame.Rect(200, 250, 140, 32)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update particle positions and apply gravitational forces
    system.apply_force()
    


    # Draw particles

    for i, p in enumerate(system.particles):
        name = p.get_name()
        x = p.get_position_x() 
        y = p.get_position_y()
        x, y = convert_to_canvas_units(x, y)
        x = x + WIDTH/2
        y = y + HEIGHT/2
        print("Particle:{}\n x: {}, y: {}".format(name,x, y))

        pygame.draw.circle(
            screen, 
            PARTICLE_COLOR[i], 
            (x, y), 
            5)
        # try:
        #     text_surface = font.render(str(round(p.get_mass()/ (10**23),2)), True, (255, 255, 255))  # Text color is white
        #     text_rect = text_surface.get_rect()
        #     text_rect.center = (int(x), int(y) +10 )  # Position below the circle
        #     screen.blit(text_surface, text_rect)
        # except:
        #     pass


    system.time = system.time + system.dt
    #system.particle_collision_2()

    text = "Time: {}  N={}".format(system.time, len(system.particles))
    text_surface = font.render(text, True, (255, 255, 255))  # Text color is white
    text_rect = text_surface.get_rect()
    #text_rect.center = (WIDTH +100, HEIGHT + 100)
    text_rect.topleft = (10, 10)
    
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    clock.tick(60)
    #time_lib.sleep(1)

pygame.quit()

