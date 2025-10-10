import pygame.key

from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/Player.png')
        self.rect = self.surf.get_rect(topleft=(350, 390))
        self.speed = 4

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if pressed_key[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def draw(self, surface):
        surface.blit(self.surf, self.rect)
