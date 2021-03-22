"""@package docstring
Documentation for this module.
 
Display Menu class
Author: Dev^(enthusiases)
This class is responsible for displaying different menus on the game screen.
"""

import pygame
from LoadAssets import *


## This is a class used to control the flow at different menus
class DisplayMenu():

    ## Constructor used to initialize the screen where the menus will be drawn 
    # @param window : the game screen, a pygame.display object, where elements are drawn
    def __init__(self, window):
        self.__game_screen = window

    ## Method used to display the main menu on the screen
    # @param main_menu_img : the image of the main menu
    def display_main_menu(self, main_menu_img):
        self.__game_screen.blit(main_menu_img, (0,0))

    ## Method used to display the pause menu on the screen
    # @param main_menu_img : the image of the pause menu
    def display_pause_menu(self, pause_menu_img):
        self.__game_screen.blit(pause_menu_img, (0,0))

    ## Method used to display the end menu on the screen
    # @param end_menu_img : the image of the end menu
    def display_end_menu(self, end_menu_img):
        self.__game_screen.blit(end_menu_img, (0,0))

    ## Method used to display the setting menu on the screen
    # @param setting_menu_img : the image of the main menu
    def display_setting_menu(self, setting_menu_img):
        self.__game_screen.blit(setting_menu_img, (0,0))
    