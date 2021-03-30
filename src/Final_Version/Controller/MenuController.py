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
        
    def setting_menu(self, play_sound, setting_menu_img):
        running = True

        current_background = play_sound.get_background()
        current_sound_effect = play_sound.get_sound_effect()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        play_sound.set_sound_effect(current_sound_effect)
                        play_sound.set_background(current_background)

                        print(play_sound.get_sound_effect(), play_sound.get_background())
                        pygame.mixer.stop()
                        play_sound.play_bg_music()
                    
                    elif event.key == pygame.K_q:
                        running = False

            current_sound_effect, current_background = self.__display_menu.display_setting_menu(play_sound, current_sound_effect, current_background, setting_menu_img)

            pygame.display.update()

    ## @brief method responsible for the instructions game screen
    def instruction_menu(self, instruction_menu_img):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        running = False
            self.__display_menu.display_instruction_menu(instruction_menu_img)
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
