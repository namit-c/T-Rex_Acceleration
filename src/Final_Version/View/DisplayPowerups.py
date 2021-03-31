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
import Powerups
import DetectCollision

## This is a class for powerups displaying
class DisplayPowerups():

    POWERUPS_WIDTH = 65
    POWERUPS_HEIGH = 65
    INTERVAL_TIME = 1
    RANDOMNESS = 0.01
    RANDOM_MIN = 3
    RANDOM_MAX = 5
    ## @brief Constructor of for DisplayPowerups class 
    #  @param game_screen the game screen, a pygame.display object, where powerups are drawn
    #  @exception Exception IllegalArgumentException
    def __init__(self, game_screen):
        if (game_screen is None):
            raise Exception("IllegalArguemntException")
        self.__game_screen = game_screen
        self.__powerups_displayed = pygame.sprite.Group()
        self.__generate_time = time.time()

    ## @brief Get the list of powerups on the screen
    #  @return return the list of powerups on the screen
    def get_powerups_list(self):
        return self.__powerups_displayed

    ## @brief Remove a powerup from the list
    #  @param p the powerup to be removed
    def remove_powerups(self, p):
        self.__powerups_displayed.remove(p)

    ## @brief Randomly generate a powerup
    #  @param speed the speed of the powerup
    def generate_powerups(self, speed, obstacles, obstacle_spawn_time):
        current_time = time.time()
        if (current_time >= self.__generate_time + random.randint(DisplayPowerups.RANDOM_MIN, DisplayPowerups.RANDOM_MAX) and current_time - obstacle_spawn_time >= DisplayPowerups.INTERVAL_TIME and random.random() < DisplayPowerups.RANDOMNESS):
            overlapping = False
            new_powerups = Powerups.Powerups(self.__game_screen, DisplayPowerups.POWERUPS_WIDTH, DisplayPowerups.POWERUPS_HEIGH  , speed)
            for obstacle in obstacles:
                if DetectCollision.detect_collision(obstacle, new_powerups):
                    overlapping = True
            if not overlapping:
                self.__powerups_displayed.add(new_powerups)
                self.__generate_time = time.time()

    ## @brief Draw a powerup on the screen
    #  @param powerups the powerup to be drawn
    def draw_powerups(self, powerups):
        for p in powerups:
            self.__game_screen.blit(p.get_img(), p.get_rect())

    ## @brief Update the position and draw all powerups in the list
    def update_powerups(self, obstacles):
        for element in self.__powerups_displayed:
            overlapping = DetectCollision.find_collision(element, obstacles)
            self.remove_powerups(overlapping)
            element.update()
            if element.get_rect().right < 0:
                self.__powerups_displayed.remove(element)

    ## @brief Update the speed of all powerups on the screen
    #  @param speed the new speed of these powerups
    def update_speed(self, speed):
        for element in self.__powerups_displayed:
            element.set_speed(speed)
