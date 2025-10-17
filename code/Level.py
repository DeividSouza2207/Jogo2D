import random
import sys
from pygame.font import Font

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_WHITE, WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY
from code.Enemy import Enemy
from code.EntityMediator import EntityMediator

from code.Player import Player


class Level:

    def __init__(self, window, name, game_mode):

        self.entity_list = []
        self.timeout = 40000  # 20s
        self.window = window
        self.name = name
        self.game_mode = game_mode
        #fundo
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)
        #jogdor
        self.player = Player('Player', (350, 390))
        self.entity_list = [self.player]  # cria a lista já com o player dentro
        pygame.time.set_timer(EVENT_ENEMY, 2000)



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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                        self.entity_list.extend(self.player.shoots[-1:])
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    y_pos = 50
                    spacing = 60
                    for i in range(5):
                        x_pos = WIN_WIDTH + (i * spacing)
                        enemy = Enemy('Enemy', (x_pos, y_pos))
                        self.entity_list.append(enemy)

            #entrada do player
            self.player.move()
            # desenha o fundo
            self.window.blit(source=self.surf, dest=self.rect)
            # desenha jogador por cima do fundo
            self.player.draw((self.window))
            # desenha inimigos
            for enemy in self.entity_list[:]:
                if isinstance(enemy, Enemy):
                    enemy.move()
                    enemy.draw(self.window)

                    # Tiro aleatório
                    if random.randint(0, 2000) < 5:
                        enemy.shoot()

                    for shot in enemy.shoots[:]:
                        shot.move()
                        shot.draw(self.window)

                        if shot.off_window():
                            enemy.shoots.remove(shot)
                            continue

                        if shot.rect.colliderect(self.player.rect):
                            self.player.health -= 1
                            enemy.shoots.remove(shot)



            for shoot in self.player.shoots[:]:
                shoot.move()
                if shoot.off_window():
                    self.player.shoots.remove(shoot)
                else:
                    shoot.draw(self.window)


            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            #self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            # collisions
            EntityMediator.verify_collision(self.entity_list, self.player)
            EntityMediator.verify_health(entity_list=self.entity_list)

            if remaining <= 0:
                print('Acabou o tempo')
                break

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
