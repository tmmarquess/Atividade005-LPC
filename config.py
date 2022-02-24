# Screen dimensions
import pygame

# Defining the screen setup
screen_width = 500
screen_height = 700

# Define the timer witch spawns an obstacle in ms
obstacle_timer_time = 500

# defines the max of bullets that can be on the screen at the same time
max_bullets_per_time = 3

# Define how many times the screen refreshes per second
fps = 60


# Initialize pygame and returns a screen instance
def initialize_screen():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    return screen
