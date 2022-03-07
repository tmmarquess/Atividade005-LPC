import pygame
import config
import obstacle
import bullet
import player

# Get the initialized Screen instance
screen = config.initialize_screen()

# Defining the font 
font = pygame.font.Font("font/retro_gaming.ttf", 30)

# Defining the initial Score
score = 0
score_text = font.render(f"Score: {score}", True, "white")
score_text_rect = score_text.get_rect()
score_text_rect.midleft = (5, 30)

# Defining the life counter
lives_text = font.render(f"Lives: {config.lives}", True, "white")
lives_text_rect = lives_text.get_rect()
lives_text_rect.midright = (config.screen_width - 5, 30)

# Start message
help_text = font.render(f"Press F to start the game", True, "white")
help_text_rect = help_text.get_rect()
help_text_rect.center = (config.screen_width // 2, config.screen_height // 2)

# Defining last attempt message
attempt = 0
last_score = font.render(f"You lost! Score: {score}", True, "white")
last_score_rect = last_score.get_rect()
last_score_rect.center = (config.screen_width // 2, (config.screen_height // 2) + 50)

# Defines if the game is active
game_active = False

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


def update_last_score_text():
    global last_score, last_score_rect, score

    last_score = font.render(f"You lost! Score: {score}", True, "white")
    last_score_rect = last_score.get_rect()
    last_score_rect.center = (config.screen_width // 2, (config.screen_height // 2) + 50)


def player_death():
    global game_active, attempt
    game_active = False

    config.reset_variables()

    obstacles.empty()
    bullets.empty()

    attempt += 1

    update_last_score_text()
    reset_score()


# Update score
def update_score():
    global score_text, score, score_text_rect

    score += 1
    score_text = font.render(f"Score: {score}", True, "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.midleft = (5, 30)


def reset_score():
    global score_text, score, score_text_rect

    score = 0
    score_text = font.render(f"Score: {score}", True, "white")
    score_text_rect = score_text.get_rect()
    score_text_rect.midleft = (5, 30)


# Update the lives
def update_lives():
    global lives_text, lives_text_rect

    config.lives -= 1

    lives_text = font.render(f"Lives: {config.lives}", True, "white")
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.midright = (config.screen_width - 5, 30)

    if config.lives == 0:
        player_death()


# Shoots a bullet, but there's a maximum
# of "max_bullets_per_time" bullets on the screen
def add_bullet():
    global game_active
    if game_active is True:
        global bullets

        if len(bullets.sprites()) <= config.max_bullets_per_time:
            bullets.add(bullet.Bullet(gamer.sprite.get_top_coordinates()))
            sound_shoot.play()


# Adds an obstacle every time the event is triggered
def add_obstacle():
    global game_active
    if game_active is True:
        global obstacles
        obstacles.add(obstacle.Obstacle())


# Increase the amount of obstacles on the screen when the event is triggered
def increase_obstacles():
    global game_active
    if config.obstacle_timer_time >= 800 and game_active is True:
        config.obstacle_timer_time *= 0.98
        config.obstacle_timer_time = int(config.obstacle_timer_time)
        pygame.time.set_timer(obstacle_timer, config.obstacle_timer_time)


# increase the speed of the next bullets that are going to spawn
def increase_speed():
    global game_active
    if config.initial_speed != 10 and game_active is True:
        config.initial_speed += config.speed_increase
        sound_speed.play()


# Check if one of the events happens
def check_events():
    global game_active

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
                if game_active is not True:
                    game_active = True
                    reset_score()
                else:
                    add_bullet()

        # increase the amount of obstacles
        if event.type == obstacle_timer_amount:
            increase_obstacles()

        # increase the speed of the comets
        if event.type == obstacle_timer_speed:
            increase_speed()


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

    # Lives
    screen.blit(lives_text, lives_text_rect)

    # Start text
    if game_active is not True:
        screen.blit(help_text, help_text_rect)

        if attempt != 0:
            screen.blit(last_score, last_score_rect)
