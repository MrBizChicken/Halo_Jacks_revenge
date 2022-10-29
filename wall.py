import pygame, random
from constants import *
import player
import random

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y + 5
        self.width = 20
        self.height = 150
        self.speed = 2
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 255 ,0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)



    def move_down(self):
        pass

    def move_up(self):
        pass

    def update(self, main_group):
        pass
