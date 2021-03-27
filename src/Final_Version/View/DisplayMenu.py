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
    def display_end_menu(self, current_score, high_score, end_menu_img):
        self.__game_screen.blit(end_menu_img, (0,0))
        self.display_msg(str(current_score), (350, 220))
        self.display_msg(str(high_score), (350, 350))
    
    ## Method used to display the setting menu on the screen
    # @param setting_menu_img : the image of the main menu
    def display_setting_menu(self, play_sound):
        font = pygame.font.SysFont('arial', 100) 
        self.__game_screen.fill((255,255,255))

        button1_sound_effect = [223, 337]
        button2_sound_effect = [385, 337]

        button1_background = [223, 100]
        button2_background = [385, 100]
        
        button_sound_action = self.buttons_setting(font, button1_sound_effect, button2_sound_effect)
        current_sound = play_sound.get_sound_effect()
        if (button_sound_action != None):
            current_sound = play_sound.get_sound_effect()
            if (button_sound_action == "+"):
                if (current_sound + 0.25 <= 1.0):
                    current_sound = current_sound + 0.25
                    #play_sound.set_sound_effect(current_sound + 0.25)
                else:
                    current_sound = 1.0
                    #play_sound.set_sound_effect(1.0)
            elif (button_sound_action == "-"):
                if (current_sound - 0.25 >= 1.0): 
                    current_sound = current_sound - 0.25
                else:
                    current_sound = 0.0
        textFont = pygame.font.SysFont('arial', 50)
        self.__game_screen.blit(textFont.render("Sound Effect Volume:", True, (0,0,0)), ((button1_sound_effect[0]+button2_sound_effect[0])/2, 250))
        self.__game_screen.blit(textFont.render(str(round(current_sound*100)), True, (0,0,0)), ((button1_sound_effect[0]+button2_sound_effect[0] - 30)/2, 375))
   
        button_sound_action = self.buttons_setting(font, button1_background, button2_background)
        current_background = play_sound.get_background()
        if (button_sound_action != None):
            current_background = play_sound.get_background()
            if (button_sound_action == "+"):
                if (current_background + 0.25 <= 1.0):
                    current_background = current_background + 0.25
                    #play_sound.set_sound_effect(current_sound + 0.25)
                else:
                    current_background = 1.0
                    #play_sound.set_sound_effect(1.0)
            elif (button_sound_action == "-"):
                if (current_background - 0.25 >= 1.0): 
                    current_background = background - 0.25
                else:
                    current_background = 0.0
        textFont = pygame.font.SysFont('arial', 50)
        self.__game_screen.blit(textFont.render("Background Volume:", True, (0,0,0)), ((button1_background[0]+button2_background[0])/2, 50))
        self.__game_screen.blit(textFont.render(str(round(current_background*100)), True, (0,0,0)), ((button1_background[0]+button2_background[0] - 30)/2, 125 ))



    # for the button on the main menu
    def buttons_setting(self, font, button1_pos, button2_pos):
        mouse_position = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          # the play button

        if button1_pos[0] - 50 < mouse_position[0] and mouse_position[0] < button1_pos[1] + 50 and button1_pos[1] - 50 < mouse_position[1] and mouse_position[1] < button1_pos[1] + 50:
          if mouse_clicked[0] == 1:
              return "-"
          #pygame.draw.rect(screen, (255, 255, 255),(215,327,70,30))

          # the quit button
        if  button2_pos[0] - 50 < mouse_position[0] and mouse_position[0] < button2_pos[0] + 50 and button2_pos[1] - 50 < mouse_position[1] and mouse_position[1] < button2_pos[1] + 50:
          if mouse_clicked[0] == 1:
              return "+"

          # text on buttons
        self.__game_screen.blit(font.render('-', True, (0,0,0)), (button1_pos[0], button1_pos[1]))
        self.__game_screen.blit(font.render('+', True, (0,0,0)), (button2_pos[0], button2_pos[1]))
        return None
    
    # for the button on the main menu
    def buttons_sound_effect(self, font):
        mouse_position = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          # the play button

        if 213 < mouse_position[0] and mouse_position[0] < 213+100 and 327 < mouse_position[1] and mouse_position[1] < 327+50:
          if mouse_clicked[0] == 1:
              return "-"
          #pygame.draw.rect(screen, (255, 255, 255),(215,327,70,30))

          # the quit button
        if 372 < mouse_position[0] and mouse_position[0] < 372+100 and 327 < mouse_position[1] and mouse_position[1] < 327+50:
          if mouse_clicked[0] == 1:
              return "+"

          # text on buttons
        self.__game_screen.blit(font.render('-', True, (0,0,0)), (223, 337))
        self.__game_screen.blit(font.render('+', True, (0,0,0)), (385, 337))
        return None



    def display_resume_menu(self, time):
        self.display_msg("Resuming Back in " + str(time), (250, 250)) 


    def display_msg(self, msg, msg_pos):
       	pygame.font.init() # you have to call this at the start, 
        my_font = pygame.font.Font("../assets/Acceleration-Reaction.ttf", 50)
        text_surface = my_font.render(msg, True, (255,255,255))
        self.__game_screen.blit(text_surface,msg_pos)
 
