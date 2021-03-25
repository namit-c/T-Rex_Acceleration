"""@package docstring
Documentation for this module.
 
Display Environment class
Author: Dev^(enthusiases)
This class is responsible for drawing the background elements on the screen.
"""

import pygame
## This is class used to draw environment elements on the screen
class DisplayEnvironment():

    ## Constructor the intitalize the game screen
    # @param window : the pygame screen that elements will be drawn on
    def __init__(self, window):
        
        ## Defining variables used in the class

        # Position to the draw the floor
        self.__Y_POS = 500
        self.__X_OFFSET = 800

        # Values of the red, blue, and green field
        # FIX CONSTANTS
        self.__RED = 0
        self.__GREEN = 1
        self.__BLUE = 2 

        self.__game_screen = window


    ## @brief display a message(string) to draw on screen 
    #  @param msg String
    #  @param msg_pos a tuple of (x,y) position to be drawn on screen
    def display_msg(self, msg, msg_pos):
       	pygame.font.init() # you have to call this at the start, 
        my_font = pygame.font.Font('../assets/Sangharia Demo.ttf', 50)
        text_surface = my_font.render(msg, True, (255, 255, 255))
        self.__game_screen.blit(text_surface,msg_pos)

    ## @brief drawing the score onto the screen
    #  @param score Score object
    def draw_score(self, score, clock):
        self.display_msg("Score: " + str(score), (250,10)) 
        self.display_msg("FPS: " + str(int(clock.get_fps())), (10,10)) 

    ## @brief drawing the game instructions onto the screen
    #  @param instructions String
    def draw_instruction(self, instructions):
        self.display_msg(instructions, (25,80)) 
    
    ## Method that draws the floor image on the game screen
    # @param floor : the image of the floor to be drawn on the screen
    # @param floor_position : the x position of the left side of the floor
    # @exception ValueError : if the floor image does not exist (NULL)
    def draw_floor(self, floor, floor_position):
        if not floor:
            raise ValueError("Floor image is NULL")
        else:
            self.__game_screen.blit(floor, (floor_position, self.__Y_POS))
            self.__game_screen.blit(floor, (floor_position + self.__X_OFFSET, self.__Y_POS))


    ## Method that draws the background on the game screen
    # @param background : the background image of the background
    # @param bg_rgb : a tuple of integers that represent that current rgb (red, green,
    # and blue) of the background
    # @exception ValueError : if the background image does ot exist (NULL)
    def draw_background(self, background, bg_rgb):
        if not background:
            raise ValueError("Background image is NULL")
        else:
            self.__game_screen.fill((bg_rgb[self.__RED], bg_rgb[self.__GREEN], bg_rgb[self.__BLUE])) 
            self.__game_screen.blit(background, (0,0))
    

