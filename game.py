import pygame
import config
import obstacle
import bullet
import player

# Get the initialized Screen instance
screen = config.initialize_screen()

# Defining the font 
font = pygame.font.Font("font/retro_gaming.ttf", 40)

# Defining the initial Score
score = 0
score_text = font.render(str(score), True, "white")
score_text_rect = score_text.get_rect()
score_text_rect.center = (250, 30)

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

# Creating an event that increases the amount of obstacles
# on the screen every "obstacle_timer_amount_time" ms
obstacle_timer_amount = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer_amount, config.obstacle_timer_amount_time)

# Creating an event that increases the speed of obstacles
# on the screen every "obstacle_timer_speed_time" ms
obstacle_timer_speed = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_timer_speed, config.obstacle_timer_speed_time)

# Defining the game sounds
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

sound_collision = pygame.mixer.Sound("sounds/collision.wav")
sound_collision.set_volume(0.1)

sound_shoot = pygame.mixer.Sound("sounds/shoot.mpeg")
sound_shoot.set_volume(0.05)

sound_speed = pygame.mixer.Sound("sounds/speed.mpeg")
sound_speed.set_volume(0.05)


# Check collision between bullet and obstacle,
# and kills them both if they collide
def bullet_obstacle_collide():
    for bullet in bullets.sprites():
        collision = pygame.sprite.spritecollide(bullet, obstacles, True)

        if collision:
            bullet.kill()
            sound_collision.play()
            update_score()


# Update score
def update_score():
    global score_text, score, score_text_rect

    score += 1
    score_text = font.render(str(score), True, "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (250, 30)


# Shoots a bullet, but there's a maximum
# of "max_bullets_per_time" bullets on the screen
def add_bullet():
    global bullets

    if len(bullets.sprites()) <= config.max_bullets_per_time:
        bullets.add(bullet.Bullet(gamer.sprite.get_top_coordinates()))
        sound_shoot.play()


# Adds an obstacle every time the event is triggered
def add_obstacle():
    global obstacles
    obstacles.add(obstacle.Obstacle())


# Increase the amount of obstacles on the screen when the event is triggered
def increase_obstacles():
    if config.obstacle_timer_time >= 800:
        config.obstacle_timer_time *= 0.98
        config.obstacle_timer_time = int(config.obstacle_timer_time)
        pygame.time.set_timer(obstacle_timer, config.obstacle_timer_time)


# increase the speed of the next bullets that are going to spawn
def increase_speed():
    if config.initial_speed != 10:
        config.initial_speed += config.speed_increase


# Check if one of the events happens
def check_events():
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

        # increase the amount of obstacles
        if event.type == obstacle_timer_amount:
            increase_obstacles()

        # increase the speed of the comets
        if event.type == obstacle_timer_speed:
            increase_speed()
            sound_speed.play()


# Draws all the screen elements
def draw_screen_elements():
    # Background
    screen.blit(config.bg, (0, 0))

    # Bullets
    bullets.draw(screen)
    bullets.update()

    # ship
    gamer.draw(screen)
    gamer.update()

    # Obstacles
    obstacles.draw(screen)
    obstacles.update()

    # Score
    screen.blit(score_text, score_text_rect)
