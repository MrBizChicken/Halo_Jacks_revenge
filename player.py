import pygame, random
from constants import *
import player
pygame.init()
from main_entity import Main_entity


class Player(Main_entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.speed = 5
        self.x_speed = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.lift = -1.5
        self.grav = 0.3
        self.vel = 0
        self.max_vel = -7
        self.direction = pygame.math.Vector2(0, 0)
        self.ability = ["human", "slime", "werewolf", "zombie"]
        self.can_jump = True
        self.jump_counter = 0
        self.clock = pygame.time.Clock()
        self.time_passed = 0
        self.facing_direction = pygame.math.Vector2(0, 0)
        self.direction  = pygame.math.Vector2(0, 0)
        self.current_ability = self.ability[0]
        self.is_fly = False
        self.hostile_mobs_passive_toggle = False



    def update(self, main_group):
        solid_objects_group = main_group.solid_objects_group
        self.ability_changer(solid_objects_group)
        self.gravity()
        self.collide(main_group)
        self.key_input(solid_objects_group, main_group)
        self.move(solid_objects_group, self.speed)


    def key_input(self, solid_objects_group, main_group):

        keys = pygame.key.get_pressed()
        player_group = main_group.player_group


        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_direction = pygame.math.Vector2(-1, 0)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1

            self.facing_direction = pygame.math.Vector2(1, 0)


        else:
            self.direction = pygame.math.Vector2(0, 0)


        if keys[pygame.K_1]:
            self.current_ability = self.ability[0]

        if keys[pygame.K_2]:
            self.current_ability = self.ability[1]

        if keys[pygame.K_3]:
            self.current_ability = self.ability[2]

        if keys[pygame.K_4]:
            self.current_ability = self.ability[3]

        if keys[pygame.K_f]:
            self.is_fly = True

        if keys[pygame.K_g]:
            self.is_fly = False




        self.x_speed *= 0.95 ** (100 * self.time_passed)

        self.rect.x += self.x_speed * self.time_passed

        self.time_passed = self.clock.tick() / 1000

        if keys[pygame.K_SPACE]:
            self.jump()
            self.jump_counter += 1



    def jump(self):
        if self.can_jump == True:
            self.vel += self.lift



    def ability_changer(self, solid_objects_group):
        if self.current_ability == self.ability[0]:
            #human

            self.height = 64
            self.rect.y + 24
            self.speed = 5
            self.max_vel = -7
            self.rect.height = 64
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((255, 255 ,255))

        if self.current_ability == self.ability[1]:
            #slime
            #bug when change to human you fall through
            self.height = 24
            self.max_vel = -7
            self.speed = 5
            self.rect.height = 24
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((255, 255 ,255))
            #make collison work later finish the rest of ability


        if self.current_ability == self.ability[2]:
            self.max_vel = -10
            self.rect.y + 24
            self.speed = 7
            self.height = 64
            self.rect.height = 64
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((255, 255 ,255))

        if self.current_ability == self.ability[3]:
            #zombie
            self.hostile_mobs_passive_toggle = False
            self.height = 64
            self.speed = 5
            self.rect.y + 24
            self.max_vel = -7
            self.rect.height = 64
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill((255, 255 ,255))




    def gravity(self):


        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel < self.max_vel:
            self.vel = self.max_vel
            self.can_jump = False



    def collide(self, main_group):
        floor_group = main_group.floor_group
        wall_group = main_group.wall_group
        self_group = main_group.player_group
        platforms = pygame.sprite.spritecollide(self, floor_group, False)

        for f in platforms:

            if self.rect.bottom < f.rect.bottom:

                self.rect.bottom = f.rect.top
                self.vel = 0
                self.can_jump = True
                self.jump_counter = 0

        walls = pygame.sprite.spritecollide(self, wall_group, False)
