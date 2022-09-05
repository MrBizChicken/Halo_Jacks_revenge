from constants import *
import sys, pygame, player


class Group_manager:
    def __init__(self):

        self.player_group = pygame.sprite.Group()
        self.floor_group = pygame.sprite.Group()
        self.drawable_objects = pygame.sprite.Group()
        self.main_group = self.update_main_group()





    def update(self):
        self.main_group = self.update_main_group()
        self.player_group.update(self)
        self.floor_group.update(self)


    def get_drawing_group(self):
        self.drawable_objects.empty()
        self.drawable_objects.add(
            self.player_group,
            self.floor_group

        )
        return self.drawable_objects

    def get_group(self, search):
        return self.main_group[search]

    def get_main_group(self):
        return self.main_group

    def update_main_group(self):
        return {
            "player_group" : self.player_group,
            "floor_group" : self.floor_group,



        }
