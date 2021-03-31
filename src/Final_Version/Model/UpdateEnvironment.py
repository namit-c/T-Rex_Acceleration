"""@package docstring
Documentation for this module.
 
UpdateEnvironment class
Author: Dev^(enthusiases)
This class is responsible for updating the floor and background colour throughtout
the game.
"""

import pygame
from random import randint

##
# @file UpdateEnvironment.py
# @brief This class is used to update the position of the floor and the colour of the 
#  background

class UpdateEnvironment():
    
    # Values of the red, blue, and green field
    RED = 0
    GREEN = 1
    BLUE = 2 

    # Max rbg value
    MAX_RGB = 255

    # Constants regarding the change the rbg values of the background
    CHANGE_BG_INTERVAL = 50
    CHANGE_BG_VAL = 50


    def __init__ (self):
        pass
        
    # @brief Method that updates the left most position of the floor
    # @param floor_position : an integer that represents the x-axis value of the
    # left most position of the floor
    # @param movement_speed : an integer that represents the how much the floor moves
    # every frame
    # @return the updated floor position
    def update_floor(self, floor_position, movement_speed):
        # Return 0 if the floor position is to the left of the boundary or
        # else return the updated floor position
        if floor_position <= UpdateEnvironment.BOUNDARY_LEFT:
            return 0
        else:
            return floor_position-movement_speed


    # @brief Method that changes the background colour during the gameplay
    # @param current_score : the current score of the player; an integer
    # @param previous_score : the previous score of the player; an integer
    # @param bg_rgb : a tuple of integers that represent that current rgb (red, green,
    # and blue) of the background
    # @return the rbg values of the next background colour
    def update_bg_colour(self, current_score, previous_score, bg_rgb):
        # Check whether the score has updated, is a multiple of 50, and is not 0
        if (round(previous_score) != round(current_score) and round(current_score) % UpdateEnvironment.CHANGE_BG_INTERVAL == 0 and round(current_score) != 0):
            randomRGBChange = randint(1,3)      # Randomly select which value to change
            if (randomRGBChange == 1):
                bg_rgb[UpdateEnvironment.RED] = (bg_rgb[UpdateEnvironment.RED] + UpdateEnvironment.CHANGE_BG_VAL) % UpdateEnvironment.MAX_RGB  # Increment value of red
            elif (randomRGBChange == 2):
                bg_rgb[UpdateEnvironment.GREEN] = (bg_rgb[UpdateEnvironment.GREEN] + UpdateEnvironment.CHANGE_BG_VAL) % UpdateEnvironment.MAX_RGB  # Increment value of blue
            else:
                bg_rgb[UpdateEnvironment.BLUE] = (bg_rgb[UpdateEnvironment.BLUE] + UpdateEnvironment.CHANGE_BG_VAL) % UpdateEnvironment.MAX_RGB  # Increment value of green
        return bg_rgb
