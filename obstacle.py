import pygame
import config
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/asteroide 2 teste.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(randint(40, config.screen_width - 40), -20))
        self.speed = config.ini_vel

    def movement(self):
        self.rect.y += self.speed

        if self.rect.top > config.screen_height + 10:
            self.kill()

    def update(self):
        self.movement()