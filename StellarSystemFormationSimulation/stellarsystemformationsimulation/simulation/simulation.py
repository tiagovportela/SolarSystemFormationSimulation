import pygame

from simulation import constants
from simulation import utilities

from system.system import System
from particles.particles import Particle



def run():
    pygame.init()


    # create a window
    screen = pygame.display.set_mode(
        (constants.Window.WIDTH, constants.Window.HEIGHT)
        )
    pygame.display.set_caption('Stellar System Formation Simulation')

    # create a clock
    clock = pygame.time.Clock()

    #control loop
    running = True

    NUMBER_OF_PARTICLES = 500
    dt = 2592000
    START_TIME = 0
    system = System(START_TIME, dt)
    system.create_particle(NUMBER_OF_PARTICLES)

    COLOR_LIST = [utilities.random_color() for i in range(NUMBER_OF_PARTICLES)]

    # main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill the screen with the background color
        screen.fill(constants.Window.BACKGROUND_COLOR)

        # draw the particles
        particles = system.get_particles()
        for i, particle in enumerate(particles):
            x = utilities.units_converter(particle.get_position_x()) + constants.Window.WIDTH/2
            y = utilities.units_converter(particle.get_position_y()) + constants.Window.HEIGHT/2
            print("Name: ", particle.get_name())
            print("x:{} y:{}".format(x,y))
            pygame.draw.circle(
                screen, 
                COLOR_LIST[i], 
                (x,y), 
                int(5)
                )
        
        system.apply_force()
        system.time = system.time + system.dt

        pygame.display.flip()
        clock.tick(60)


pygame.quit()
        




