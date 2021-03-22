import pygame
import time
from time import *

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, char_img):
        pygame.sprite.Sprite.__init__(self)
        if(screen is None or char_img is None):
            raise Exception("IllegalArgumentException")
        self.screen = screen
        self.image = pygame.transform.scale(char_img,(75,75))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + 99
        self.rect.bottom = self.screen_rect.bottom - 80
        self.is_ducking = False
        self.is_jumping = False
        self.is_invincible = False
        self.is_double_jumping = False
        self.is_slo_mo = False
        self.movement = [0,0]
        self.__jumping_limit = 0
        self.__time = 0
  
    def get_rect(self):
        return self.rect

    def get_img(self):
        return self.image

    def set_img(self, new_img):
        if(new_img is None):
            raise Exception("IllegalArgumentException")        
        self.image = pygame.transform.scale(new_img, (75,75))
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom - 99
        self.rect.left = self.screen_rect.left + 100
    
    def set_ducking_img(self, new_img):
        if(new_img is None):
            raise Exception("IllegalArgumentException")       
        self.image = pygame.transform.scale(new_img, (85,35))
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom - 99
        self.rect.left = self.screen_rect.left + 100     
    
    def duck(self, ducking_img, inv_ducking_img):
        if(ducking_img is None or inv_ducking_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False:
            self.is_ducking = True
            if self.is_invincible == False:
                self.set_ducking_img(ducking_img)
            else: 
                self.set_ducking_img(inv_ducking_img)

    def stand(self, inv_char, char_img):
        if(inv_char is None or char_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False:
            self.is_ducking = False
            if self.is_invincible == False:
                self.set_img(char_img)
            else:
                self.set_img(inv_char)

    def jump(self, inv_jumping_char, jumping_img):
        if(inv_jumping_char is None or jumping_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False and self.is_ducking == False:
            self.is_jumping = True
            self.movement[1] = -25
            self.__jumping_limit += 1
        if self.is_double_jumping == True and self.is_jumping == True and self.__jumping_limit < 3:
            self.__jumping_limit += 1
            self.movement[1] = -20

    ## private method
    def checkbounds(self):
        if self.rect.bottom > self.screen_rect.bottom - 99:
            self.rect.bottom = self.screen_rect.bottom - 99
            self.is_jumping = False
            self.__jumping_limit = 0

    def invincible(self, inv_char):
        if(inv_char is None):
            raise Exception("IllegalArgumentException")
        self.__time = pygame.time.get_ticks()
        self.is_invincible = True
        self.is_double_jumping = False
        self.is_slo_mo = False
        self.set_img(inv_char)

    def double_jump(self):
        self.__time = pygame.time.get_ticks()
        self.is_invincible = False
        self.is_double_jumping = True
        self.is_slo_mo = False

    def slo_mo(self):
        self.__time = pygame.time.get_ticks()
        self.is_invincible = False
        self.is_double_jumping = False
        self.is_slo_mo = True

    ## private method
    def is_powered(self):
        return self.is_double_jumping or self.is_invincible or self.is_slo_mo

    def update(self, char_img):
        if self.is_jumping:
            self.movement[1] += 1
        self.rect = self.rect.move(self.movement)   
        self.checkbounds()
        if self.__time + 5000 < pygame.time.get_ticks() and self.is_powered():
            self.is_invincible = False
            self.is_double_jumping = False
            self.is_slo_mo = False
            left = self.rect.left
            bottom = self.rect.bottom
            if(char_img is None):
                raise Exception("IllegalArgumentException")       
            self.image = pygame.transform.scale(char_img, (85,35))
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.bottom = bottom

