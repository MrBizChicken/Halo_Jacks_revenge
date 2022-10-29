from constants import *
import sys, pygame, player


class Group_manager:
    def __init__(self):

        self.player_group = pygame.sprite.Group()
        self.floor_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.drawable_objects = pygame.sprite.Group()
        self.main_group = self.update_main_group()
        self.solid_objects_group = pygame.sprite.Group()
        self.portal1_group = pygame.sprite.Group()
        self.portal2_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
        self.test_enemy_group = pygame.sprite.Group()




    def update(self):
        self.main_group = self.update_main_group()
        self.player_group.update(self)
        self.solid_objects_group.add(self.floor_group, self.wall_group, self.test_enemy_group)
        self.portal_group.add(self.portal1_group, self.portal2_group)
        self.portal_group.update(self)
        self.solid_objects_group.update(self)
        self.floor_group.update(self)
        self.test_enemy_group.update(self)
        self.wall_group.update(self)


    def get_drawing_group(self):
        self.drawable_objects.empty()
        self.drawable_objects.add(
            self.player_group,
            self.floor_group,
            self.wall_group,
            self.solid_objects_group,
            self.portal_group


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
            "wall_group" : self.wall_group,
            

        }
