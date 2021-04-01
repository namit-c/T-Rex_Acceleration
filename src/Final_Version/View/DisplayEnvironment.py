"""@package docstring
Documentation for this module.
 
Display Environment class
Author: Dev^(enthusiases)
This class is responsible for drawing the background elements on the screen.
"""

import pygame

##
# @file DisplayEnvironment.py
# @brief This class is responsible for maintaining instructions, score and background  


## This is class used to draw environment elements on the screen
class DisplayEnvironment():
    ## Defining variables used in the class
    # Position to the draw the floor
    Y_POS = 500
    X_OFFSET = 800
    # FIX CONSTANTS
    RED = 0
    GREEN = 1
    BLUE = 2 
    WHITE = (255,255,255)
    FONTSIZE = 50
    FPS_POS = (10,10)
    SCORE_POS = (250,10)
    BG_POS = (0,0)
    POWERUP_POS = (100,200)
    
    ## @brief Constructor the intitalize the game screen
    # @param window the pygame screen that elements will be drawn on
    def __init__(self, window):
        self.__game_screen = window

    ## @brief Displaying a message(string) to draw on screen 
    #  @param msg String
    #  @param msg_pos a tuple of (x,y) position to be drawn on screen
    def display_msg(self, msg, msg_pos):
       	pygame.font.init() # you have to call this at the start, 
        my_font = pygame.font.Font('../assets/Sangharia Demo.ttf', DisplayEnvironment.FONTSIZE)
        text_surface = my_font.render(msg, True, DisplayEnvironment.WHITE)
        self.__game_screen.blit(text_surface,msg_pos)

    ## @brief Drawing the score onto the screen
    #  @param score Score object
    def draw_score(self, score, clock):
        self.display_msg("Score: " + str(score), DisplayEnvironment.SCORE_POS) 
        self.display_msg("FPS: " + str(int(clock.get_fps())), DisplayEnvironment.FPS_POS) 
    
    ## @brief Drawing the floor image on the game screen
    #  @param floor the image of the floor to be drawn on the screen
    #  @param floor_position the x position of the left side of the floor
    #  @exception ValueError if the floor image does not exist (NULL)
    def draw_floor(self, floor, floor_position):
        if not floor:
            raise ValueError("Floor image is NULL")
        else:
            self.__game_screen.blit(floor, (floor_position, DisplayEnvironment.Y_POS))
            self.__game_screen.blit(floor, (floor_position + DisplayEnvironment.X_OFFSET, DisplayEnvironment.Y_POS))


    ## @brief Drawing the background on the game screen
    #  @param background the background image of the background
    #  @param bg_rgb a tuple of integers that represent that current rgb (red, green,
    #  and blue) of the background
    #  @exception ValueError if the background image does ot exist (NULL)
    def draw_background(self, background, bg_rgb):
        if not background:
            raise ValueError("Background image is NULL")
        else:
            self.__game_screen.fill((bg_rgb[DisplayEnvironment.RED], bg_rgb[DisplayEnvironment.GREEN], bg_rgb[DisplayEnvironment.BLUE])) 
            self.__game_screen.blit(background, DisplayEnvironment.BG_POS)
    
    ## @brief Drawing the powerup-time remaining onto the screen
    #  @param time The remaining time of the powerup
    def draw_powerup(self, time):
        self.display_msg("Time Remaining: " + str(time), DisplayEnvironment.POWERUP_POS)