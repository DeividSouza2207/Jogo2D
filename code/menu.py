

import pygame.image
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, C_GREEN, MENU_OPTION, C_WHITE, C_YELLOW, C_GRAY


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=70, text="SPACE", text_color=C_GREEN, text_center_pos=((WIN_WIDTH / 2), 100))
            self.menu_text(text_size=70, text="WARS", text_color=C_GREEN, text_center_pos=((WIN_WIDTH / 2), 180))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=C_YELLOW, text_center_pos=((WIN_WIDTH / 2), 300 + 30 * i))
                else:
                    self.menu_text(text_size=30, text=MENU_OPTION[i], text_color=C_WHITE, text_center_pos=((WIN_WIDTH / 2), 300 + 30 * i))

            self.menu_text(text_size=20, text="SPACE - atirar", text_color=C_GRAY, text_center_pos=((WIN_WIDTH / 2), 450))
            self.menu_text(text_size=20, text="KEY_RIGHT - vai para a direita", text_color=C_GRAY,text_center_pos=((WIN_WIDTH / 2), 475))
            self.menu_text(text_size=20, text="KEY_LEFT - vai para a esquerda", text_color=C_GRAY,text_center_pos=((WIN_WIDTH / 2), 500))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fecha a janela
                    quit()  # encerra o pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN: # enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
