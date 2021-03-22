"""@package docstring
Documentation for this module.
 
DisplayCharacter class
Author: Dev^(enthusiases)
This class is responsible for displaying the character on the screen.
"""

import sys
sys.path.insert(1, '../Model')
from Character import *

## This is a class for the character displaying
class DisplayCharacter():

    ## @brief Constructor of for DisplayCharacter class 
    #  @param window : the game screen, a pygame.display object, where the character is drawn
    #  @param character : the character object to be drawn
    def __init__(self, window, character):
        self.game_screen = window
        self.game_character = character

    ## @brief draw the character onto the screen
    def draw_character(self):
        self.game_screen.blit(self.game_character.get_img(), self.game_character.get_rect())
        pygame.draw.rect(self.game_screen, (255,0,0), self.game_character.get_rect(), 2)
