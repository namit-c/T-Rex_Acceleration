"""@package docstring
Documentation for this module.
 
Display Environment class
Author: Dev^(enthusiases)
This class is responsible for drawing the background elements on the screen.
"""

import pygame

## This is class used to draw environment elements on the screen
class DipslayEnvironment():

    ## Defining variables used in the class

    # Position to the draw the floor
    Y_POS = 450
    X_OFFSET = 800

    # Values of the red, blue, and green field
    RED = 0
    GREEN = 1
    BLUE = 2 

    ## Constructor the intitalize the game screen
    # @param window : the pygame screen that elements will be drawn on
    def __init__(self, window, ):
        self.__game_screen = window

    ## Draw score
    def draw_score(score):
        pass

    ## Draw instructions
    def draw_instruction(instructions):
        pass

    ## Method that draws the floor image on the game screen
    # @param floor : the image of the floor to be drawn on the screen
    # @param floor_position : the x position of the left side of the floor
    # @exception ValueError : if the floor image does not exist (NULL)
    def draw_floor(floor, floor_position):
        if not floor:
            raise ValueError("Floor image is NULL")
        else:
            self.__game_screen.blit(floor, (floor_position, Y_POS))
            self.__game_screen.blit(floor, (floor_position + X_OFFSET, Y_POS))


    ## Method that draws the background on the game screen
    # @param background : the background image of the background
    # @param bg_rgb : a tuple of integers that represent that current rgb (red, green,
    # and blue) of the background
    # @exception ValueError : if the background image does ot exist (NULL)
    def draw_background(background, bg_rgb):
        if not background:
            raise ValueError("Background image is NULL")
        else:
            self.__game_screen.fill(bg_rgb[RED], bg_rgb[GREEN], bg_rgb[BLUE])
            self.__game_screen(background, (0,0))
            