import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coord: tuple):
        super().__init__()
        self.image = pygame.Surface((15, 20))
        self.image.fill("red")
        self.rect = self.image.get_rect(midbottom=coord)
        self.speed = 7

    def movement(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

    def update(self):
        self.movement()
