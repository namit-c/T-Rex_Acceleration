"""@package docstring
Documentation for this module.
 
Obstacle class
Author: Dev^(enthusiases)
This class is responsible for maintaining several properties of the obstacle object
"""

import pygame

##
# @file Obstacle.py
# @brief This class is responsible for maintaining several properties of the obstacle object  


## This class is used to maintain key properties of an obstacle such as the width, height, 
#  speed and pygame.image
class Obstacle(pygame.sprite.Sprite):
    
    ## @brief Constructor for Obstacle class
    #  @param width width of image of obstacle
    #  @param height height of image of obstacle
    #  @param obstacle_img pygame.image 
    def _init_(self, name, width, height, speed, obstacle_img):
        super()._init_()
        self.__name = name
        self.__width = width
        self.__height = height
        self.__speed = speed
        self.__img = obstacle_img
        self.__rect = obstacle_img.get_rect()


    ## @brief get the width of an obstacle
    #  @return return the width of an  width
    def get_width(self):
        return self.__width

    ## @brief change the width of an obstacle
    #  @param width new width to set the current width to
    #  @exception ValueError Invalid Width: Should be greater than or equal to zero"
    def set_width(self, width):
        if (width < 0):
            raise ValueError("Invalid Width: Should be greater than or equal to zero")
        self.__width = width
    
    ## @brief get the height of an obstacle
    #  @return return the height of an obstacle
    def get_height(self):
        return self.__height
   
    ## @brief change the height of an obstacle
    #  @param height new height to set the current height to
    #  @exception ValueError Invalid Height: Should be greater than or equal to zero
    def set_height(self, height):
        if (height < 0):
            raise ValueError("Invalid Height: Should be greater than or equal to zero")
        self.__height = height
    

    ## @brief get the speed of an obstacle
    #  @return return the speed of an obstacle
    def get_speed(self):
        return self.__speed

    ## @brief change the speed of an obstacle
    #  @param new_speed new speed to set the current speed to
    #  @exception ValueError new_speed is less than 0 (meaning opposite direction)
    def set_speed(self, new_speed):
        if (new_speed < 0):
            raise ValueError("Invalid Speed: Should be greather than 0")
        self.__speed = new_speed

    ## @brief get the pygame.image of obstacle
    #  @return return the pygame.image of an obstacle
    def get_img(self):
        return self.__img


    ## @brief change the pygame.image of the obstacle and update the rect of the obstacle
    #  @param new_img new image to set the current pygame.image to
    #  @exception TypeError if the new_image does not exists
    def set_img(self, new_img):
        if (new_img == None):
            raise TypeError ("Invalid Pygame.img")
        self.__img = new_img
        self.__rect = new_img.get_rect()

    ## @brief get the rectangle of an obstacle
    def get_rect(self):
        return self.__rect

    ## @brief set the corridnates of the rectangle of the obstacle to the new position
    #  @param x new x position for the rectangle
    #  @param y new y position for the rectangle
    def set_rect(self, x, y):
        self.__rect.left = x
        self.__rect.bottom = y + self.get_height() 

