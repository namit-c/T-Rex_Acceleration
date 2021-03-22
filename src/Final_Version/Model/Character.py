"""@package docstring
Documentation for this module.
 
Character class
Author: Dev^(enthusiases)
This class is responsible for maintaining several properties and methods of the character object
"""

import pygame
import time
from time import *

##
# @file Character.py
# @brief This class is responsible for maintaining several properties and methods of the character object  


## This class is used to maintain key properties of a character such as pygame.image, pygame.rect, 
#  and powerups related properties like is_invincible. It also contains some necessary methods like duck and jump
class Character(pygame.sprite.Sprite):

    NORMAL_SIZE = (75,75)
    DUCKING_SIZE = (85,35)
    X_OFFSET = 99
    Y_OFFSET = 80
    JUMPING_SPEED = -25
    DOUBLEJUMPING_SPEED = -20
    GRAVITY = 1
    DURARION = 5000

    ## @brief Constructor for Character class
    #  @param screen screen on which the character is shown
    #  @param char_img pygame.image 
    def __init__(self, screen, char_img):
        pygame.sprite.Sprite.__init__(self)
        if(screen is None or char_img is None):
            raise Exception("IllegalArgumentException")
        self.screen = screen
        self.image = pygame.transform.scale(char_img, Character.NORMAL_SIZE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + Character.X_OFFSET
        self.rect.bottom = self.screen_rect.bottom - Character.Y_OFFSET
        self.is_ducking = False
        self.is_jumping = False
        self.is_invincible = False
        self.is_double_jumping = False
        self.is_slo_mo = False
        self.movement = [0,0]
        self.__jumping_limit = 0
        self.__time = 0

    ## @brief getter, get the rect of the character
    #  @return return the rect of the character  
    def get_rect(self):
        return self.rect

    ## @brief getter, get the image of the character
    #  @return return the image of the character  
    def get_img(self):
        return self.image

    ## @brief change the image of the character
    #  @param new_img new img to set the current image to
    #  @param bot the bottom position of the image
    #  @param lefg the left position of the image
    #  @exception Exception IllegalArguementException 
    def set_img(self, new_img, bot, left):
        if(new_img is None):
            raise Exception("IllegalArgumentException")        
        self.image = pygame.transform.scale(new_img, Character.NORMAL_SIZE)
        self.rect = self.image.get_rect()
        self.rect.bottom = bot
        self.rect.left = left

    ## @brief change the image of the character in ducking size
    #  @param new_img new image to set the current image to
    #  @param bot the bottom position of the image
    #  @param lefg the left position of the image
    #  @exception Exception IllegalArguementException     
    def set_ducking_img(self, new_img, bot, left):
        if(new_img is None):
            raise Exception("IllegalArgumentException")       
        self.image = pygame.transform.scale(new_img, Character.DUCKING_SIZE)
        self.rect = self.image.get_rect()
        self.rect.bottom = bot
        self.rect.left = left 

    ## @brief make the character duck 
    #  @param ducking_img new image to show the ducking
    #  @param inv_ducking_img new image to show the ducking, invincible version
    #  @exception Exception IllegalArguementException     
    def duck(self, ducking_img, inv_ducking_img):
        if(ducking_img is None or inv_ducking_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False:
            self.is_ducking = True
            if self.is_invincible == False:
                self.set_ducking_img(ducking_img, self.screen_rect.bottom - Character.Y_OFFSET, self.screen_rect.left + Character.X_OFFSET)
            else: 
                self.set_ducking_img(inv_ducking_img, self.screen_rect.bottom - Character.Y_OFFSET, self.screen_rect.left + Character.X_OFFSET)

    ## @brief make the character stand up after ducking 
    #  @param inv_char new image to show the character, invincible version
    #  @param char_img new image to show the character
    #  @exception Exception IllegalArguementException 
    def stand(self, inv_char, char_img):
        if(inv_char is None or char_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False:
            self.is_ducking = False
            if self.is_invincible == False:
                self.set_img(char_img, self.screen_rect.bottom - Character.Y_OFFSET, self.screen_rect.left + Character.X_OFFSET)
            else:
                self.set_img(inv_char, self.screen_rect.bottom - Character.Y_OFFSET, self.screen_rect.left + Character.X_OFFSET)

    ## @brief make the character jump
    #  @param inv_ducking_img new image to show the jumping, invincible version
    #  @param ducking_img new image to show the jumping
    #  @exception Exception IllegalArguementException 
    def jump(self, inv_jumping_char, jumping_img):
        if(inv_jumping_char is None or jumping_img is None):
            raise Exception("IllegalArgumentException")
        if self.is_jumping == False and self.is_ducking == False:
            self.is_jumping = True
            self.movement[1] = Character.JUMPING_SPEED
            self.__jumping_limit += Character.GRAVITY
        if self.is_double_jumping == True and self.is_jumping == True and self.__jumping_limit < 3:
            self.__jumping_limit += Character.GRAVITY
            self.movement[1] = Character.DOUBLEJUMPING_SPEED

    ## @brief private method, reset the character if it is back to ground
    def checkbounds(self):
        if self.rect.bottom > self.screen_rect.bottom - Character.X_OFFSET:
            self.rect.bottom = self.screen_rect.bottom - Character.X_OFFSET
            self.is_jumping = False
            self.__jumping_limit = 0

    ## @brief make the character invincible
    #  @param inv_char new image to show invincibility of the character
    #  @exception Exception IllegalArguementException 
    def invincible(self, inv_char):
        if(inv_char is None):
            raise Exception("IllegalArgumentException")
        self.__time = pygame.time.get_ticks()
        self.is_invincible = True
        self.is_double_jumping = False
        self.is_slo_mo = False
        self.set_img(inv_char, self.screen_rect.bottom - Character.Y_OFFSET, self.screen_rect.left + Character.X_OFFSET)

    ## @brief allow the character to do double jump
    def double_jump(self):
        self.__time = pygame.time.get_ticks()
        self.is_invincible = False
        self.is_double_jumping = True
        self.is_slo_mo = False

    ## @brief allow the character to slow the obstacles and powerups down
    def slo_mo(self):
        self.__time = pygame.time.get_ticks()
        self.is_invincible = False
        self.is_double_jumping = False
        self.is_slo_mo = True

    ## @brief private method, check if the character gets a special ability
    #  @return return True if the character gets a special ability
    def is_powered(self):
        return self.is_double_jumping or self.is_invincible or self.is_slo_mo

    ## @brief update the position, status and image of the character
    #  @param char_img the image the character after the powerup runs out
    #  @exception Exception IllegalArguementException 
    def update(self, char_img):
        if self.is_jumping:
            self.movement[1] += Character.GRAVITY
        self.rect = self.rect.move(self.movement)   
        self.checkbounds()
        if self.__time + Character.DURARION < pygame.time.get_ticks() and self.is_powered():
            self.is_invincible = False
            self.is_double_jumping = False
            self.is_slo_mo = False
            left = self.rect.left
            bottom = self.rect.bottom
            if(char_img is None):
                raise Exception("IllegalArgumentException")       
            self.image = pygame.transform.scale(char_img, Character.NORMAL_SIZE)
            self.set_img(char_img, bottom, left)


