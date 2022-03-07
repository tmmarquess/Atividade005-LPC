import pygame

# Background
bg = pygame.image.load('img/Background.png')

# Defining the screen setup
screen_width = bg.get_width()
screen_height = bg.get_height()


# If you want to change these values, change then inside this function
def reset_variables():
    global lives, obstacle_timer_time, obstacle_timer_speed_time, initial_speed
    global speed_increase, obstacle_timer_amount_time, max_bullets_per_time, fps

    # Defines how many lives the player has on the game
    lives = 3

    # Define the timer witch spawns an obstacle in ms
    obstacle_timer_time = 1500

    # defines the timer that updates the obstacle speed in ms
    obstacle_timer_speed_time = 10000

    # Defines the initial speed of an obstacle
    initial_speed = 2

    # Defines how much the obstacle speed increases when the event triggers
    speed_increase = 0.5

    # defines the timer that updates the obstacle spawn timer in ms
    obstacle_timer_amount_time = 10000

    # defines the max of bullets that can be on the screen at the same time
    max_bullets_per_time = 3

    # Define how many times the screen refreshes per second
    fps = 60


lives = None

obstacle_timer_time = None

obstacle_timer_speed_time = None

initial_speed = None

speed_increase = None

obstacle_timer_amount_time = None

max_bullets_per_time = None

fps = None


# Initialize pygame and returns a screen instance
def initialize_screen():
    global bg

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Mission")
    bg = bg.convert()

    reset_variables()

    return screen
