import pygame
import config
import obstacle
import bullet
import player
pygame.init()
score = 0
WHITE = (255, 255, 255)
# Sounds
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)
sound_collision = pygame.mixer.Sound("sounds/collision.wav")
sound_shoot = pygame.mixer.Sound("sounds/shoot.mpeg")
sound_shoot.set_volume(0.1)
sound_speed = pygame.mixer.Sound("sounds/speed.mpeg")
sound_speed.set_volume(0.1)

# Check collision between bullet and obstacle,
# and kills them both if they collide
def bullet_obstacle_collide(score):
    for bullet in bullets.sprites():
        collision = pygame.sprite.spritecollide(bullet, obstacles, True)
        if collision:
            bullet.kill()
            sound_collision.play()
            update_score()

# Update score
def update_score():
    global text, score, textRect
    score += 1
    text = font.render(str(score), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (250, 30)

# Shoots a bullet, but there's a maximum
# of 3 bullets on the screen
def add_bullet():
    global bullets
    if len(bullets.sprites()) <= config.max_bullets_per_time:
        bullets.add(bullet.Bullet(gamer.sprite.get_top_coordinates()))
        sound_shoot.play()


# Adds an obstacle every time the event is triggered
def add_obstacle():
    global obstacles
    obstacles.add(obstacle.Obstacle())



# Get the initialized Screen instance
screen = config.initialize_screen()

# Text screen 
font = pygame.font.Font("font/retro_gaming.ttf", 40)
text = font.render(str(score), True, WHITE)
textRect = text.get_rect()
textRect.center = (250, 30)

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

obstacle_timer_qtd = pygame.USEREVENT + 2
pygame.time.set_timer(obstacle_timer_qtd, config.obstacle_timer_qtd)

obstacle_timer_vel = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_timer_vel, config.obstacle_timer_vel)

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

        # increase the quantity of comets
        if event.type == obstacle_timer_qtd:
            config.obstacle_timer_time *= 0.98
            config.obstacle_timer_time = int(config.obstacle_timer_time)
            pygame.time.set_timer(obstacle_timer, config.obstacle_timer_time)
            print(config.obstacle_timer_time)

        # increase the speed of the comets
        if event.type == obstacle_timer_vel:
            config.ini_vel += config.dt_vel
            sound_speed.play()


    # Drawing the elements on the screen
    screen.blit(config.bg, (0, 0))
    screen.blit(text, textRect)

    bullets.draw(screen)
    bullets.update()

    gamer.draw(screen)
    gamer.update()

    obstacles.draw(screen)
    obstacles.update()

    # Checking the collision between a bullet and an obstacle
    bullet_obstacle_collide(score)

    # Update pygame screen
    pygame.display.update()

    # defines how many refreshes per second happens
    clock.tick(config.fps)
