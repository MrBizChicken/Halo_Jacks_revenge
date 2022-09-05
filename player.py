from constants import *
import pygame


import pygame, random
from constants import *
import player
pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.lift = -1
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -7
        self.direction = pygame.math.Vector2(0, 0)

        self.can_jump = True
        self.jump_counter = 0




    def update(self, main_group):
        self.key_input()
        self.gravity()
        self.collide(main_group)


    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:


            if self.rect.y > 0:
                self.rect.y += -self.speed



        if keys[pygame.K_DOWN]:
            if self.rect.bottom < GAME_HEIGHT:
                self.rect.y += self.speed



        if keys[pygame.K_LEFT]:

            if self.rect.x > 0:
                self.rect.x += -self.speed




        if keys[pygame.K_RIGHT]:
            if self.rect.right < GAME_HEIGHT:
                self.rect.x += self.speed




        if keys[pygame.K_SPACE]:
            self.jump()
            self.jump_counter += 1


    def jump(self):
        if self.can_jump == True:
            self.vel += self.lift



    def gravity(self):


        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel < self.max_vel:
            self.vel = self.max_vel
            self.can_jump = False



    def collide(self, main_group):
        floor_group = main_group.floor_group
        self_group = main_group.player_group
        platforms = pygame.sprite.spritecollide(self, floor_group, False)

        for c in platforms:

            if self.rect.bottom < c.rect.bottom:

                self.rect.bottom = c.rect.top
                self.vel = 0
                self.can_jump = True
                self.jump_counter = 0
