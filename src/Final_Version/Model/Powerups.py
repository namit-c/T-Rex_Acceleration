"""@package docstring
Documentation for this module.
 
Powerups class
Author: Dev^(enthusiases)
This class is responsible for maintaining several properties of the Powerups object
"""

import pygame
import random
import sys
sys.path.insert(1, '../View')
import LoadAssets

##
# @file Powerups.py
# @brief This class is responsible for maintaining several properties of the Powerups object  


## This class is used to maintain key properties of a Powerups such as the width, height, 
#  speed and screen
class Powerups(pygame.sprite.Sprite):

    Y_OFFSET = 100
    TPYES = 3
        
    ## @brief Constructor for Powerups class
    #  @param screen screen on which the powerups will be shown
    #  @param width width of image of powerup
    #  @param height height of image of powerup
    #  @param speed speed of powerups
    def __init__(self, screen, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.__screen = screen 
        self.__name = random.randint(0,Powerups.TPYES)
        self.__width = width
        self.__height = height
        assets = LoadAssets()
        self.__image = pygame.transform.scale(assets.load_all_powerups()[self.__name], (width, height))
        self.rect = self.__image.get_rect()
        self.__screen_rect = screen.get_rect()
        self.rect.left = self.__screen_rect.right
        self.rect.bottom = self.__screen_rect.bottom - Powerups.Y_OFFSET 
        self.__speed = speed

    ## @brief Get the rect of a powerup
    #  @return the rect of a powerup
    def get_rect(self):
        return self.rect

    ## @brief Get the width of a powerup
    #  @return the width of an powerup
    def get_width(self):
        return self.__width

    ## @brief Change the width of an obstacle
    #  @param width new width to set the current width to
    #  @exception Exception IllegalArgumentException
    def set_width(self, new_width):
        if (new_width < 0):
            raise Exception("IllegalArgumentException")
        self.__width = new_width

    ## @brief Get the height of a powerup
    #  @return the height of a powerup
    def get_height(self):
        return self.__height

    ## @brief Change the height of a powerup
    #  @param height new height to set the current height to
    #  @exception Exception IllegalArgumentException
    def set_height(self, new_height):
        if (new_height < 0):
            raise Exception("IllegalArgumentException")
        self.__height = new_height

    ## @brief Get the speed of a powerup
    #  @return the speed of a powerup
    def get_speed(self):
        return self.__speed

    ## @brief Change the speed of a powerup
    #  @param new_speed new speed to set the current speed to
    def set_speed(self, new_speed):
        self.__speed = new_speed

    ## @brief Get the pygame.image of powerup
    #  @return the pygame.image of a powerup
    def get_img(self):
        return self.__image

    ## @brief Change the pygame.image of the powerup
    #  @param new_powerup_img new image to set the current pygame.image to
    #  @exception Exception IllegalArgument
    def set_image(self, new_powerup_img):
        if (new_powerup_img is None):
            raise Exception("IllegalArgumentException")
        self.__image = new_powerup_img

    ## @brief Get the name(index) of the powerup
    #  @return return the index representing the name
    def get_name(self):
        return self.__name   

    ## @brief Update the postion of a powerup
    def update(self):
        self.rect = self.rect.move([self.__speed,0])

