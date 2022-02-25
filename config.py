# Screen dimensions
import pygame

# Background
bg = pygame.image.load('img/Background.png')

# Defining the screen setup
screen_width = bg.get_width()
screen_height = bg.get_height()

# Define the timer witch spawns an obstacle in ms
obstacle_timer_time = 500

# atualiza veloc
obstacle_timer_vel = 2000
ini_vel = 2
dt_vel = 0.5

# atualiza qtd
obstacle_timer_qtd = 2000

# defines the max of bullets that can be on the screen at the same time
max_bullets_per_time = 3

# Define how many times the screen refreshes per second
fps = 60


# Initialize pygame and returns a screen instance
def initialize_screen():
    global bg
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    bg = bg.convert()
    return screen
