"""@package docstring
Documentation for this module.
 
Display Menu class
Author: Dev^(enthusiases)
This class is responsible for displaying different menus on the game screen.
"""

import pygame
from LoadAssets import *
import sys
import time

##
# @file DisplayEnvironment.py
# @brief This is a class used to control the flow at different menus

class DisplayMenu():
    ## @brief Constructor used to initialize the screen where the menus will be drawn 
    # @param window the game screen, a pygame.display object, where elements are drawn
    def __init__(self, window):
        self.__game_screen = window
        
        # Defining constants for the position and the colour
        self.__BLACK = (0, 0, 0)
        self.__WHITE = (255, 255, 255)
        self.__TOP_LEFT_POSITION = (0, 0)
        self.__END_SCREEN_CR_POS = (350, 220)
        self.__END_SCREEN_HR_POS = (350, 350)

    ## @brief Method used to display the main menu on the screen
    # @param main_menu_img  the image of the main menu
    def display_main_menu(self, main_menu_img):
        self.__game_screen.blit(main_menu_img, self.__TOP_LEFT_POSITION)

    ## @brief Method used to display the pause menu on the screen
    # @param main_menu_img the image of the pause menu
    def display_pause_menu(self, pause_menu_img):
        self.__game_screen.blit(pause_menu_img, self.__TOP_LEFT_POSITION)

    ## @brief Method used to display the end menu on the screen
    #  @param current_score current score the user has achieved
    #  @param high_score highest score the user has achieved since the start of the game running 
    #  @param end_menu_img the image of the end menu
    def display_end_menu(self, current_score, high_score, end_menu_img):
        self.__game_screen.blit(end_menu_img, self.__TOP_LEFT_POSITION)
        self.display_msg(str(current_score), self.__END_SCREEN_CR_POS)
        self.display_msg(str(high_score), self.__END_SCREEN_HR_POS)
    
    ## @brief Method used to display the instructions menu on the screen
    #  @param instruction_menu_img the image of the instructions menu
    def display_instruction_menu(self, instruction_menu_img):
        self.__game_screen.blit(instruction_menu_img, self.__TOP_LEFT_POSITION)

    ## @brief Method used to display the setting menu on the screen, handle button events for user increasing and decreasing the volume 
    #  setting for background and sound effect
    #  @param initial_sound_effect inital sound effect volume setting when user joins the settings menu
    #  @param initial_background intial background volume setting when user joins the settings menu
    #  @param setting_menu_img the image of the setting menu
    def display_setting_menu(self, play_sound, initial_sound_effect, initial_background, setting_menu_img):
        # Constants for the position of the buttons
        SOUND_EFFECT_MINUS_VOL = [223, 337]
        SOUND_EFFECT_PLUS_VOL = [385, 337]
        BG_MUSIC_MINUS_VOL = [223, 180]
        BG_MUSIC_PLUS_VOL = [385, 180]

        # Constants for indexing the lists
        WIDTH = 0
        HEIGHT = 1

        # Constants for volume
        CHANGE_IN_VOLUME_SE = 0.1
        CHANGE_IN_VOLUME_BG = 0.05
        MAX_VOLUME = 1.0
        MIN_VOLUME = 0.0

        # Constant for the time button needs to register the input properly
        BUTTON_REGISTER_TIME = 0.3

        DECIMAL_TO_PERCENT = 100
        
        BUTTON_SIZE = 100
        self.__game_screen.blit(setting_menu_img, self.__TOP_LEFT_POSITION)
        button_font = pygame.font.SysFont('arial', BUTTON_SIZE)
        
        # Drawing and handling input for the sound effect volume buttons
        button_sound_action = self.buttons_setting(button_font, SOUND_EFFECT_MINUS_VOL, SOUND_EFFECT_PLUS_VOL)
        current_sound = initial_sound_effect 
        if (button_sound_action != None):
            if (button_sound_action == "+"):
                if (current_sound + CHANGE_IN_VOLUME_SE <= MAX_VOLUME):
                    current_sound = current_sound + CHANGE_IN_VOLUME_SE
                    #play_sound.set_sound_effect(current_sound + 0.25)
                else:
                    current_sound = MAX_VOLUME
                    #play_sound.set_sound_effect(1.0)
                time.sleep(BUTTON_REGISTER_TIME)
            elif (button_sound_action == "-"):
                if (current_sound - CHANGE_IN_VOLUME_SE >= MIN_VOLUME): 
                    current_sound = current_sound - CHANGE_IN_VOLUME_SE
                else:
                    current_sound = MIN_VOLUME
                time.sleep(BUTTON_REGISTER_TIME)

        # Drawing text for the sound effect volums
        TEXT_FONT_SIZE = 50
        text_font = pygame.font.SysFont('arial', TEXT_FONT_SIZE)
        self.__game_screen.blit(text_font.render("Sound Effect Volume:", True, self.__BLACK), ((SOUND_EFFECT_MINUS_VOL[WIDTH]+\
            SOUND_EFFECT_PLUS_VOL[WIDTH])/2 - 100, 275))
        self.__game_screen.blit(text_font.render(str(round(current_sound*DECIMAL_TO_PERCENT)), True, self.__BLACK), \
            ((SOUND_EFFECT_MINUS_VOL[HEIGHT]+SOUND_EFFECT_PLUS_VOL[HEIGHT] - 30)/2, 375))
   
        # Drawing and handling input for the background music volume buttons 
        button_sound_action = self.buttons_setting(button_font, BG_MUSIC_MINUS_VOL, BG_MUSIC_PLUS_VOL)
        current_background = initial_background 
        if (button_sound_action != None):
            if (button_sound_action == "+"):
                if (current_background + CHANGE_IN_VOLUME_BG <= MAX_VOLUME):
                    current_background = current_background + CHANGE_IN_VOLUME_BG
                    #play_sound.set_sound_effect(current_sound + 0.25)
                else:
                    current_background = MAX_VOLUME
                    #play_sound.set_sound_effect(1.0)
                time.sleep(BUTTON_REGISTER_TIME)
            elif (button_sound_action == "-"):
                if (current_background - CHANGE_IN_VOLUME_BG >= MIN_VOLUME): 
                    current_background = current_background - CHANGE_IN_VOLUME_BG
                else:
                    current_background = MIN_VOLUME

                time.sleep(BUTTON_REGISTER_TIME)

        self.__game_screen.blit(text_font.render("Background Volume:", True, self.__BLACK), ((BG_MUSIC_MINUS_VOL[WIDTH]+BG_MUSIC_MINUS_VOL[WIDTH])/2\
             - 100, 150))
        self.__game_screen.blit(text_font.render(str(round(current_background*DECIMAL_TO_PERCENT)), True, self.__BLACK), \
            ((BG_MUSIC_PLUS_VOL[WIDTH]+BG_MUSIC_PLUS_VOL[WIDTH] - 30)/2, 220 ))
        
        return current_sound, current_background

    ## @brief General button placement for displaying two buttons - the plus and minus buttons. Handles event if one specific button has been pressed
    #  @param font pygame.font for displaying the plus and minus symbols
    #  @param button1_pos list of two elements x and y value for the first button which is the minus button
    #  @param button2_pos list of two elements x and y value for the second button which is the plus button 
    def buttons_setting(self, font, button1_pos, button2_pos):
        mouse_position = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        # Constants for indexing the lists
        FIRST = 0
        SECOND = 1

        # Constant for the size of the button
        BUTTON_MARGIN = 100

        if button1_pos[FIRST] < mouse_position[FIRST] and mouse_position[FIRST] < button1_pos[FIRST] + BUTTON_MARGIN and button1_pos[SECOND] < mouse_position[SECOND] and \
            mouse_position[SECOND] < button1_pos[SECOND] + BUTTON_MARGIN:
          if mouse_clicked[FIRST] == 1:
              return "-"
          #pygame.draw.rect(screen, (255, 255, 255),(215,327,70,30))

        # The quit button
        if  button2_pos[FIRST]  < mouse_position[FIRST] and mouse_position[FIRST] < button2_pos[FIRST] + BUTTON_MARGIN and button2_pos[SECOND]  < mouse_position[SECOND] and \
            mouse_position[SECOND] < button2_pos[SECOND] + BUTTON_MARGIN:
          if mouse_clicked[FIRST] == 1:
              return "+"

        # Text on buttons
        self.__game_screen.blit(font.render('-', True, self.__BLACK), (button1_pos[FIRST], button1_pos[SECOND]))
        self.__game_screen.blit(font.render('+', True, self.__BLACK), (button2_pos[FIRST], button2_pos[SECOND]))
        return None
   

    ## @brief displaying the amount of time left till the game resume back
    #  @param time current time remaining
    def display_resume_menu(self, time):
        MSG_POS = (250, 250)
        self.display_msg("Resuming Back in " + str(time), MSG_POS) 

    ## @brief display a specific string message at a specific location
    #  @param msg string of message to be displayed
    #  @param msg_pos tuple of (x,y) for the message to display the message
    def display_msg(self, msg, msg_pos):
       	pygame.font.init() # You have to call this at the start 
        FONT_SIZE = 50
        my_font = pygame.font.Font("../assets/Acceleration-Reaction.ttf", FONT_SIZE)
        text_surface = my_font.render(msg, True, self.__WHITE)
        self.__game_screen.blit(text_surface,msg_pos)