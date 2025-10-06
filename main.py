import pygame

pygame.init()
window = pygame.display.set_mode(size=(700, 580))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

