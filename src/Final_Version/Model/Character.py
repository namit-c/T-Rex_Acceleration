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

    NORMAL_SIZE = (75,65)
    DUCKING_SIZE = (85,40)
    X_OFFSET = 100
    Y_OFFSET = 99
    JUMPING_SPEED = -20
    DOUBLEJUMPING_SPEED = -20
    GRAVITY = 1
    DURARION = 5000
    IMAGE_SELECTOR = 6
    DOUBLE_JUMPING_LIMIT = 2

    ## @brief Constructor for Character class
    #  @param screen screen on which the character is shown
    #  @param char_img pygame.image 
    def __init__(self, screen, char_img):
        pygame.sprite.Sprite.__init__(self)
        if(screen is None or char_img is None):
            raise Exception("IllegalArgumentException")
        self.__screen = screen
        # MADE THE IMAGE INTO A LIST; NEED TO CHANGE ALL THE IMAGE 
        self.__image = []
        for img_num in range(len(char_img)):
            self.__image.append(pygame.transform.scale(char_img[img_num], Character.NORMAL_SIZE))
        self.rect = self.__image[0].get_rect()
        self.__screen_rect = screen.get_rect()
        self.rect.left = self.__screen_rect.left + Character.X_OFFSET
        self.rect.bottom = self.__screen_rect.bottom - Character.Y_OFFSET
        self.__is_ducking = False
        self.__is_jumping = False
        self.__is_invincible = False
        self.__is_double_jumping = False
        self.__is_slo_mo = False
        self.__movement = [0,0]
        self.__jumping_limit = 0
        self.__time = 0

    ## @brief getter, get the rect of the character
    #  @return return the rect of the character  
    def get_rect(self):
        return self.rect

    ## @brief getter, get the image of the character
    #  @return return the image of the character  
    def get_img(self, img_num):
        # Changed so the image retured is a one of the images in the list
        return self.__image[img_num//Character.IMAGE_SELECTOR]

    ## @brief change the image of the character
    #  @param new_img new img to set the current image to
    #  @param bot the bottom position of the image
    #  @param lefg the left position of the image
    #  @exception Exception IllegalArguementException 

    def set_img(self, new_img, bot, left):
        if(new_img is None):
            raise Exception("IllegalArgumentException")
        # For the moving character ---- NOT YET WORKING PROPERLY
        if not isinstance(new_img, list):
            self.__image[0] = pygame.transform.scale(new_img, Character.NORMAL_SIZE)
        else:
            for img_num in range(len(self.__image)):
                self.__image[img_num] = pygame.transform.scale(new_img[img_num], Character.NORMAL_SIZE)
        self.rect = self.__image[0].get_rect()
         # ----------------------------------------------------------------
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
        # For the moving character ---- NOT YET WORKING PROPERLY
        if not isinstance(new_img, list):
            self.__image[0] = pygame.transform.scale(new_img, Character.DUCKING_SIZE)
        else:
            for img_num in range(len(self.image)):
                self.image[img_num] = pygame.transform.scale(new_img[img_num], Character.DUCKING_SIZE)
        self.rect = self.image[0].get_rect()
         # ----------------------------------------------------------------
        self.rect.bottom = bot
        self.rect.left = left 

    ## @brief make the character duck 
    #  @param ducking_img new image to show the ducking
    #  @param inv_ducking_img new image to show the ducking, invincible version
    #  @exception Exception IllegalArguementException     
    def duck(self, char_img):
        if(char_img is None):
            raise Exception("IllegalArgumentException")
        if self.__is_jumping == False:
            self.__is_ducking = True
            self.__image = [pygame.transform.scale(char_img, Character.DUCKING_SIZE)] * 8
            self.rect = self.__image[0].get_rect()
            self.rect.bottom = self.__screen_rect.bottom - Character.Y_OFFSET
            self.rect.left = self.__screen_rect.left + Character.X_OFFSET

    ## @brief getter, check if the character is ducking
    #  @return return true if the character is ducking, false otherwise 
    def get_ducking(self):
        return self.__is_ducking    

    ## @brief make the character stand up after ducking 
    #  @param inv_char new image to show the character, invincible version
    #  @param char_img new image to show the character
    #  @exception Exception IllegalArguementException 
    def stand(self, char_img):
        if(char_img is None):
            raise Exception("IllegalArgumentException")
        if self.__is_jumping == False:
            self.__is_ducking = False
            self.set_img(char_img, self.__screen_rect.bottom - Character.Y_OFFSET, self.__screen_rect.left + Character.X_OFFSET)
   
    ## @brief make the character jump
    #  @param inv_ducking_img new image to show the jumping, invincible version
    #  @param ducking_img new image to show the jumping
    #  @exception Exception IllegalArguementException 
    def jump(self, jumping_img):
        if(jumping_img is None):
            raise Exception("IllegalArgumentException")
        if self.__is_jumping == False and self.__is_ducking == False:
            self.__is_jumping = True
            self.__movement[1] = Character.JUMPING_SPEED
            self.__image = [pygame.transform.scale(jumping_img, Character.NORMAL_SIZE)] * 8
            self.rect = self.__image[0].get_rect()
            self.rect.bottom = self.__screen_rect.bottom - Character.Y_OFFSET
            self.rect.left = self.__screen_rect.left + Character.X_OFFSET
            self.__jumping_limit += 1
        if self.__is_double_jumping == True and self.__is_jumping == True and self.__jumping_limit <= Character.DOUBLE_JUMPING_LIMIT:
            self.__jumping_limit += 1
            self.__movement[1] = Character.DOUBLEJUMPING_SPEED

    ## @brief getter, check if the character is jumping
    #  @return return true if the character is jumping, false otherwise 
    def get_jumping(self):
        return self.__is_jumping 

    ## @brief private method, reset the character if it is back to ground
    def checkbounds(self):
        if self.rect.bottom > self.__screen_rect.bottom - Character.Y_OFFSET:
            self.rect.bottom = self.__screen_rect.bottom - Character.Y_OFFSET
            self.__is_jumping = False
            self.__jumping_limit = 0
                
    ## @brief make the character invincible
    #  @param inv_char new image to show invincibility of the character
    #  @exception Exception IllegalArguementException 
    def invincible(self):
        self.__time = pygame.time.get_ticks()
        self.__is_invincible = True
        self.__is_double_jumping = False
        self.__is_slo_mo = False

    ## @brief getter, check if the character is invincible
    #  @return return true if the character is invincible, false otherwise 
    def get_invincible(self):
        return self.__is_invincible         

    ## @brief allow the character to do double jump
    #  @param char_img the image of double_jumping status
    def double_jump(self):
        self.__time = pygame.time.get_ticks()
        self.__is_invincible = False
        self.__is_double_jumping = True
        self.__is_slo_mo = False

    ## @brief getter, check if the character is in double jumping status
    #  @return return true if the character jump twice, false otherwise 
    def get_double_jumping(self):
        return self.__is_double_jumping         

    ## @brief allow the character to slow the obstacles and powerups down
    #  @param char_img the image of slo_mo status
    def slo_mo(self):
        self.__time = pygame.time.get_ticks()
        self.__is_invincible = False
        self.__is_double_jumping = False
        self.__is_slo_mo = True

    ## @brief getter, check if the character is in slow motion status
    #  @return return true if the character can slow obstacles down, false otherwise 
    def get_slo_mo(self):
        return self.__is_slo_mo

    ## @brief private method, check if the character gets a special ability
    #  @return return True if the character gets a special ability
    def is_powered(self):
        return self.__is_double_jumping or self.__is_invincible or self.__is_slo_mo

    ## @brief update the position, status and image of the character
    #  @param char_img the image the character after the powerup runs out
    #  @exception Exception IllegalArguementException 
    def update(self, char_img):
        if self.__is_jumping:
            self.__movement[1] += Character.GRAVITY
        self.rect = self.rect.move(self.__movement)  
        self.checkbounds()
        if not(self.__is_jumping or self.__is_ducking):
            self.set_img(char_img, self.__screen_rect.bottom - Character.Y_OFFSET, self.__screen_rect.left + Character.X_OFFSET)
        if self.__time + Character.DURARION < pygame.time.get_ticks() and self.is_powered():
            self.__is_invincible = False
            self.__is_double_jumping = False
            self.__is_slo_mo = False

    ## @brief getter, get the number of jumps the character made
    #  @return return the number of jumops the character made
    def get_limit(self):
        return self.__jumping_limit

    ## @brief Reset the charater status when the game restarts
    def reset(self, char_img):
        self.__image = []
        for img_num in range(len(char_img)):
           self.__image.append(pygame.transform.scale(char_img[img_num], Character.NORMAL_SIZE))
        self.rect = self.__image[0].get_rect()
        self.rect.left = self.__screen_rect.left + Character.X_OFFSET
        self.rect.bottom = self.__screen_rect.bottom - Character.Y_OFFSET
        self.__is_ducking = False
        self.__is_jumping = False
        self.__is_invincible = False
        self.__is_double_jumping = False
        self.__is_slo_mo = False
        self.__movement = [0,0]
        self.__jumping_limit = 0
        self.__time = 0


