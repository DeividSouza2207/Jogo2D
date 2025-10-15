import pygame

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/Enemy.png')
        self.rect = self.surf.get_rect(topleft=(550, 10))
        self.shoots = []

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        shoot_position = self.rect.midtop
        shoot = EnemyShot('EnemyShot', shoot_position, speed=4)
        self.shoots.append(shoot)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)
        for shoot in self.shoots:
            shoot.draw(surface)