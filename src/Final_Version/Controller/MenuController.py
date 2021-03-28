"""@package docstring
Documentation for this module.
 
Menu Controller class
Author: Dev^(enthusiases)
This class is responsible for controlling the flow on the menus. It calls 
view and model modules while handling the user input.
"""
import pygame
from time import *
import sys
sys.path.insert(1, '../View')
import DisplayMenu

class MenuController:
    def __init__(self, window):
        self.__display_menu = DisplayMenu.DisplayMenu(window)
        
    def setting_menu(self, play_sound):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.__display_menu.display_setting_menu(play_sound)
            pygame.display.update()

    def end_menu(self, current_score, high_score, img):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return "Restart"
                    elif event.key == pygame.K_q:
                        sys.exit()
                        #return "Quit"
                    
    
            self.__display_menu.display_end_menu(current_score, high_score, img)
            pygame.display.update()
    
    def pause_menu(self, img):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:

                        return "Resume"
                    elif event.key == pygame.K_q:
                        return "Quit"

            self.__display_menu.display_pause_menu(img)
            pygame.display.update()

    def resume_menu(self, current_time):
        self.__display_menu.display_resume_menu(round(current_time))
        pygame.display.update()
