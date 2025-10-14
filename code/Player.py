import pygame.key
from pygame.key import get_pressed

from code.Const import PLAYER_KEY_SHOOT
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/Player.png')
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 8
        self.shoots = []

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def shoot(self):
        shoot_position = self.rect.midtop
        shoot = PlayerShot('PlayerShot', shoot_position)
        self.shoots.append(shoot)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)
        for shoot in self.shoots:
            shoot.draw(surface)

