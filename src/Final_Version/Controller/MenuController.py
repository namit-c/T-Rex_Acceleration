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
        

    def end_menu(self, score):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                  return
    
            self.__display_menu.end_menu_view(score) 
    
    def pause_menu(self):
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
            self.__display_menu.pause_menu_view()

    def resume_menu(self):
        time_now = time()

        current_time = time_now
        while (current_time - time_now <= 5):
            self.__display_menu.resume_back_view(round(5 - (current_time - time_now)))
            current_time = time()
