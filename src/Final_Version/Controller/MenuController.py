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

##
# @file MenuController.py
# @brief This class is responsible for maintaining several flow of control between different menus in the game
#        like pause, setting, instruction and end menus.

class MenuController:

    ## @brief Constructor for MenuController
    #  @param window pygame.display
    def __init__(self, window):
        self.__display_menu = DisplayMenu.DisplayMenu(window)
    
    ## @brief control the flow for the setting menu, handle save current setting button and back button events. 
    #         Saves the current settings of the background volume and sound effect volume set by the user
    #  @param play_sound PlaySound object that handles all audio properties in the game
    #  @param setting_menu_img  pygame.image of the setting menu
    def setting_menu(self, play_sound, setting_menu_img):
        running = True

        current_background = play_sound.get_background()
        current_sound_effect = play_sound.get_sound_effect()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        play_sound.set_sound_effect(current_sound_effect)
                        play_sound.set_background(current_background)

                        pygame.mixer.stop()
                        play_sound.play_bg_music()
                    
                    elif event.key == pygame.K_b:
                        running = False

            current_sound_effect, current_background = self.__display_menu.display_setting_menu(play_sound, current_sound_effect, current_background, setting_menu_img)

            pygame.display.update()

    ## @brief method responsible for the instructions game screen. Handles keybutton events for returning back to main menu
    #  @param instruction_menu_img pygame.image of the instructions menu
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

    ## @brief Control the flow for the end menu, handle input for restarting the game (return back to main menu) or quiting the game
    #  @param current_score integer of the current score the user achieved in the current game session
    #  @param high_score integer of the highest score the user has achieved overall when running the game
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
    
    ## @brief Control the flow for the pause menu, handle input for resume the game (return to current state of game) or quiting the game
    #  @param img pygame.image of the pause menu
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

    ## @brief handling resume back to the current state of the game
    #  @param current_time current count down time till current game state resumes back
    def resume_menu(self, current_time):
        self.__display_menu.display_resume_menu(round(current_time))
        pygame.display.update()
