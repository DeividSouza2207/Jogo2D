# C
import pygame

C_GREEN = (0, 255, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

#E
ENTITY_HEALTH ={
                'Player': 300,
                'Enemy': 50,
                'PlayerShot': 1,
                'EnemyShot': 1
}
ENTITY_SPEED = {'Enemy': 2,
                'PlayerShot': 5,
                'EnemyShot': 0}
EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME',
                'SCORE',
                'EXIT')

# P
PLAYER_KEY_SHOOT = {'Player': pygame.K_RCTRL}

# W
WIN_WIDTH = 800
WIN_HEIGHT = 520