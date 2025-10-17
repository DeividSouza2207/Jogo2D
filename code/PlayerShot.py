import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.Surface((4,10))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(midbottom=position)
        self.speed = 10
        self.health = 1

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def off_window(self):
        return self.rect.bottom < 0