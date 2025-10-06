import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(700, 580))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # fecha a janela
            #         quit()  # encerra o pygame