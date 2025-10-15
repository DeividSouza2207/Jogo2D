from turtle import speed

import pygame

from code.Entity import Entity

class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple, speed=1):
        super().__init__(name, position)
        self.surf = pygame.Surface((4,10))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(midbottom=position)
        self.speed = speed
        self.health = 1

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def off_window(self):
        return self.rect.top > 600
