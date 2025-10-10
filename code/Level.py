import sys
from pygame.font import Font

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:

    def __init__(self, window, name, game_mode):

        self.window = window
        self.name = name
        self.game_mode = game_mode
        #fundo
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)
        #jogdor
        self.player = Player('./asset/Player.png', (350, 390))
        self.timeout = 20000 # 20s

    def run(self):
        pygame.mixer_music.load(f'./asset/Level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        while True:
            clock.tick(60)
            timeout = pygame.time.get_ticks() - start_time
            remaining = max(0 , self.timeout - timeout)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #entrada do player
            self.player.move()
            # desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)
            # desenha jogador por cima do fundo
            self.player.draw((self.window))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            #self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            if remaining <= 0:
                print('Acabou o tempo')
                break

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
