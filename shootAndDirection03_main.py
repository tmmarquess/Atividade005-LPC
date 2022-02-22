# shoot in any direction
# pygame.mouse.get_pos()
import pygame, math, random
from square import Square
from bullet import Bullet

pygame.init()

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 500
screen_height = 800
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

#Build a square (https://pygame.readthedocs.io/en/latest/rect/rect.html)
dx_sq = 20
dy_sq = 20
x_sq = screen_width // 2
y_sq = screen_height - 2 * dy_sq
#sq_x_pos = 50
#sq_y_pos = screen_height - 50
#sq_width = 20
#sq_heigh = 20
speed = 20
sq = Square(green,x_sq,y_sq,dx_sq,dy_sq, speed,screen_width,screen_height)
#sq = Square(green,left,top,right,bottom, speed)
#sq = Square(green,200,200,100,100, 10)

bullets = []
enemies = []

#Main program loop
done = False
while not done:
    #Get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Print value of key press
            """if event.key==119: #w
                sq.direction = 'N'
            if event.key==97: #a
                sq.direction = 'W'
            if event.key==115: #s
                sq.direction = 'S'
            if event.key==100: #d
                sq.direction = 'E'"""
            if event.key == pygame.K_f: #32: #spacebar
                #Fire a bullet
                spawnx = sq.rect.x + sq.rect.width/2 - 10
                b = Square(red, spawnx,sq.rect.y, 20,20, 20,screen_width,screen_height)
                b.direction = 'N'
                bullets.append(b)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            #print(x,y)
            b = Bullet(red, sq.rect.centerx, sq.rect.centery, 20,20, 20, x,y)
            bullets.append(b)

    #Handle held down keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        sq.moveDirection('N',screen_width,dx_sq)
    if pressed[pygame.K_LEFT]:
        sq.moveDirection('W',screen_width,dx_sq)
    if pressed[pygame.K_s]:
        sq.moveDirection('S')
    if pressed[pygame.K_RIGHT]:
        sq.moveDirection('E',screen_width,dx_sq)
        
    #Update game objects
    for b in bullets:
        b.move()
    for e in enemies:
        e.move()
    #spawn enemies on the top of the screen and tell them to move down
    if random.randint(1,30) == 15: #15 doesn't matter
        x = random.randint(0,screen_width-40)
        e = Square(yellow, x,-40, 40,40, 10,screen_width,screen_height)
        e.direction = 'S'
        enemies.append(e)
    #Check for collisions
    '''for b in bullets:
        for e in enemies:
            if b.collided(e.rect):
                #e.color = white #TESTING
                enemies.remove(e)
                bullets.remove(b)'''
    for i in reversed(range(len(bullets))):
        for j in reversed(range(len(enemies))):
            if bullets[i].collided(enemies[j].rect):
                #e.color = white #TESTING
                del enemies[j]
                del bullets[i]
                break

    #All the drawing
    surface.fill(black) #fill surface with black
    for b in bullets:
        b.draw(surface)
    for e in enemies:
        e.draw(surface)
    sq.draw(surface)
    pygame.display.flip()
    pygame.event.get()
    clock.tick(50) #30 FPS
pygame.quit()
exit()
