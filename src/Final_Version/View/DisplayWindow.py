"""@package docstring
Documentation for this module.
 
DisplayWindow class
Author: Dev^(enthusiases)
This class is responsible for creating the main game window where all 
elements can be drawn.
"""

import pygame

##
# @file DisplayWindow.py
# @brief This is a class for responsible for the game window

class DisplayWindow():

    ## @brief Constructor that creates the game screen
    def __init__(self):
        ## Defining the constants for the dimensions of the screen
        WIDTH = 800
        HEIGHT = 600
        
        self.__game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ## @brief Method that returns the game window
    #  @return the game screen 
    def get_game_screen(self):
        return self.__game_screen
