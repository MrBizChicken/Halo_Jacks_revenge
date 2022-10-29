from constants import *
import pygame
import csv
import player
import floor
import wall
import portal_1
import portal_2
import test_enemy



class Load_level():
    def __init__(self):

        self.level = LEVELS

        self.level_num = 0








    def get_list(self, level):
        map_list = ""

        with open(level) as file:
            map_list = file.read().split("\n")
        # filter out all "#" and empty strings
        map_list = list(filter(self.is_comment, map_list))

        #finally split by csv
        for m in range(len(map_list)):
            map_list[m] = map_list[m].split(",")

        return map_list


    def is_comment(self, string):
        if not string:
            return False
        if string[0] == "#":
            return False
        return True

    def load_level(self, level, main_group):
        player_group = main_group.player_group
        floor_group = main_group.floor_group
        wall_group = main_group.wall_group
        portal_group = main_group.portal_group
        portal1_group = main_group.portal1_group
        portal2_group = main_group.portal2_group
        test_enemy_group = main_group.test_enemy_group

        test_enemy_group.empty()
        player_group.empty()
        portal_group.empty()
        floor_group.empty()
        wall_group.empty()


        map_tiles = self.get_list(self.level[level])
        for row in range(len(map_tiles)):
            for col in range(len(map_tiles[row])):
                item = map_tiles[row][col]



                if item == "p":


                    player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "pf":


                    floor_group.add(floor.Floor(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "w":


                    wall_group.add(wall.Wall(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "p1":


                    portal1_group.add(portal_1.Portal1(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "p2":


                    portal2_group.add(portal_2.Portal2(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "e":


                    test_enemy_group.add(test_enemy.Test_enemy(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    def clear_level(self, main_group):

        player_group = main_group.player_group
        floor_group = main_group.floor_group
        wall_group = main_group.wall_group
        portal_group = main_group.portal_group
        test_enemy_group = main_group.test_enemy_group

        test_enemy_group.empty()
        player_group.empty()
        portal_group.empty()
        floor_group.empty()
        wall_group.empty()

        self.load_level(self.level_num, main_group)
