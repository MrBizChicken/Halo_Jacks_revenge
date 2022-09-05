from constants import *
import pygame
import csv
import player
import floor



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



        player_group.empty()
        floor_group.empty()


        map_tiles = self.get_list(self.level[level])
        for row in range(len(map_tiles)):
            for col in range(len(map_tiles[row])):
                item = map_tiles[row][col]



                if item == "p":


                    player_group.add(player.Player(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                if item == "pf":
                    print("made object")

                    floor_group.add(floor.Floor(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    def clear_level(self, main_group):

        player_group = main_group.player_group
        floor_group = main_group.floor_group



        player_group.empty()
        floor_group.empty()
        self.load_level(self.level_num, main_group)
