import pygame
import config


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill("green")
        self.rect = self.image.get_rect(midbottom=(config.screen_width // 2, config.screen_height - 20))
        self.speed = 10

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

            if self.rect.left < 0:
                self.rect.left = 0

        if keys[pygame.K_d]:
            self.rect.x += self.speed

            if self.rect.right > config.screen_width:
                self.rect.right = config.screen_width

    def update(self):
        self.movement()

    def get_top_coordinates(self):
        return self.rect.midtop
