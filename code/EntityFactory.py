import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            # case 'MenuBg':
            #      list_bg = []
            #      for i in range(1):
            #          list_bg.append(Background(entity_name=f'MenuBg{i}', position=(0,0)))

            case 'Player':
                return Player('Player', (WIN_WIDTH / 2, 10))

            case 'Enemy':
                return Enemy('Enemy',(WIN_WIDTH + 50, 390))