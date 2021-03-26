"""@package docstring
Documentation for this module.
 
DisplayPowerups class
Author: Dev^(enthusiases)
This class is responsible for displaying powerups on the screen.
"""

import random
import sys
import pygame
import time
sys.path.insert(1, '../Model')
from Powerups import *
import DetectCollision

## This is a class for powerups displaying
class DisplayPowerups():

    ## @brief Constructor of for DisplayPowerups class 
    #  @param game_screen the game screen, a pygame.display object, where powerups are drawn
    #  @exception Exception IllegalArgumentException
    def __init__(self, game_screen):
        if (game_screen is None):
            raise Exception("IllegalArguemntException")
        self.game_screen = game_screen
        self.powerups_displayed = pygame.sprite.Group()
        self.__generate_time = time.time()

    ## @brief get the list of powerups on the screen
    #  @return return the list of powerups on the screen
    def get_powerups_list(self):
        return self.powerups_displayed

    ## @brief remove a powerup from the list
    #  @param p the powerup to be removed
    def remove_powerups(self, p):
        self.powerups_displayed.remove(p)

    ## @brief randomly generate a powerup
    #  @param speed the speed of the powerup
    def generate_powerups(self, speed, obstacles):
        if (time.time() >= self.__generate_time + random.randint(3,5) and random.random() < 0.01):
            overlapping = False
            new_powerups = Powerups(self.game_screen, 65, 65, speed)
            for obstacle in obstacles:
                if DetectCollision.detect_collision(obstacle, new_powerups):
                    overlapping = True
            if not overlapping:
                self.powerups_displayed.add(new_powerups)
                self.__generate_time = time.time()

    ## @brief draw a powerup on the screen
    #  @param powerups the powerup to be drawn
    def draw_powerups(self, powerups):
        self.game_screen.blit(powerups.get_img(), powerups.get_rect())

    ## @brief update the position and draw all powerups in the list
    def update_powerups(self):
        for element in self.powerups_displayed:
            self.draw_powerups(element)
            element.update()
