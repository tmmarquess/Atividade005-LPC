import pygame, math, random

class Square:
    def __init__(self, color, x, y, dx_sq, dy_sq, speed,screen_width,screen_height):
        self.rect = pygame.Rect(x,y,dx_sq, dy_sq)
        self.color = color
        self.direction = 'E'
        self.speed = speed

    def move(self):
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def moveDirection(self, direction,screen_width,dx_sq):
        if direction == 'E':
            self.rect.x = self.rect.x+self.speed
            #Check that you are not going too far (off the screen)
            if self.rect.x > screen_width - dx_sq:
              self.rect.x = screen_width - dx_sq

          
        if direction == 'W':
            self.rect.x = self.rect.x-self.speed
	    #Check that you are not going too far (off the screen)
            if self.rect.x < 0:
                self.rect.x = 0                        
        if direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def collided(self, other_rect):
        #Return True if self collided with other_rect
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
