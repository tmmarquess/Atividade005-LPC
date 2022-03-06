import pygame
import game
import config

# Gets the clock instance
clock = pygame.time.Clock()

# Game loop
while True:
    # Check if an event happens
    game.check_events()

    # Draw's all the screen elements
    game.draw_screen_elements()

    # Checking the collision between a bullet and an obstacle
    game.bullet_obstacle_collide()

    # Update pygame screen
    pygame.display.update()

    # defines how many refreshes per second happens
    clock.tick(config.fps)
