"""@package docstring
Documentation for this module.
 
DisplayWindow class
Author: Dev^(enthusiases)
This class is responsible for creating the main game window where all 
elements can be drawn.
"""

import pygame

## This is a class for the game window
def DisplayWindow():

    ## Defining the constants for the dimensions of the screen
    WIDTH = 800
    HEIGHT = 600

    ## Constructor that creates the game screen
    def __init__(self):
        self.__game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ## Method that returns the game windw
    # @return the game screen 
    def get_game_screen():
        return self.__game_screen
