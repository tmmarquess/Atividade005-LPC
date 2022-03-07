import pygame
import config
import game
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/asteroid.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(randint(40, config.screen_width - 40), 0))
        self.speed = config.initial_speed

    def movement(self):
        self.rect.y += self.speed

        if self.rect.top > config.screen_height:
            game.update_lives()
            self.kill()

    def update(self):
        self.movement()
