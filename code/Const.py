# C
import pygame.constants

C_GREEN = (0, 255, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

#E
ENTITY_HEALTH ={
                'Player': 300,
                'Enemy': 50
}
ENTITY_SPEED = {'Enemy': 2}
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME',
        'SCORE',
        'EXIT')

# W
WIN_WIDTH = 800
WIN_HEIGHT = 520