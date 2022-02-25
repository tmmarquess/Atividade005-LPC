import pygame
import config
import obstacle
import bullet
import player


# Check collision between bullet and obstacle,
# and kills them both if they collide
def bullet_obstacle_collide():
    for bullet in bullets.sprites():
        collision = pygame.sprite.spritecollide(bullet, obstacles, True)
        if collision:
            bullet.kill()


# Shoots a bullet, but there's a maximum
# of 3 bullets on the screen
def add_bullet():
    global bullets
    if len(bullets.sprites()) <= config.max_bullets_per_time:
        bullets.add(bullet.Bullet(gamer.sprite.get_top_coordinates()))


# Adds an obstacle every time the event is triggered
def add_obstacle():
    global obstacles
    obstacles.add(obstacle.Obstacle())


# Get the initialized Screen instance
screen = config.initialize_screen()

# Gets the clock instance
clock = pygame.time.Clock()

# Creating the player group
gamer = pygame.sprite.GroupSingle()
gamer.add(player.Player())

# Creating the obstacles group
obstacles = pygame.sprite.Group()

# Creating the bullets group
bullets = pygame.sprite.Group()

# Creating an event that creates a new obstacle
# on the screen every "obstacle_timer_time" ms
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, config.obstacle_timer_time)

# Game loop
while True:
    for event in pygame.event.get():
        # Check if the user wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check if the obstacle event happens
        if event.type == obstacle_timer:
            add_obstacle()

        # Check if the player shoots a bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                add_bullet()

    # Drawing the elements on the screen
    screen.blit(config.bg, (0, 0))

    bullets.draw(screen)
    bullets.update()

    gamer.draw(screen)
    gamer.update()

    obstacles.draw(screen)
    obstacles.update()

    # Checking the collision between a bullet and an obstacle
    bullet_obstacle_collide()

    # Update pygame screen
    pygame.display.update()

    # defines how many refreshes per second happens
    clock.tick(config.fps)
