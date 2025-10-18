# C
import pygame

C_GREEN = (0, 255, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GRAY = (170, 170, 170)
C_LIGHTGREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

#E
ENTITY_DAMAGE = {
    'Player': 1,
    'Enemy': 1,
    'PlayerShot': 25,
    'EnemyShot': 25
}

ENTITY_HEALTH ={
                'Player': 300,
                'Enemy': 25,
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