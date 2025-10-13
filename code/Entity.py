from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self, surface):
        pass