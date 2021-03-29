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
    def generate_powerups(self, speed, obstacles, obstacle_spawn_time):
        current_time = time.time()
        if (current_time >= self.__generate_time + random.randint(3,5) and current_time - obstacle_spawn_time >= 1 and random.random() < 0.01):
            print("POWER UP GENERATED")
            overlapping = False
            new_powerups = Powerups.Powerups(self.game_screen, 65, 65, speed)
            for obstacle in obstacles:
                if DetectCollision.detect_collision(obstacle, new_powerups):
                    overlapping = True
            if not overlapping:
                self.powerups_displayed.add(new_powerups)
                self.__generate_time = time.time()

    ## @brief draw a powerup on the screen
    #  @param powerups the powerup to be drawn
    def draw_powerups(self, powerups):
        for p in powerups:
            self.game_screen.blit(p.get_img(), p.get_rect())

    ## @brief update the position and draw all powerups in the list
    def update_powerups(self, obstacles):
        for element in self.powerups_displayed:
            #self.draw_powerups(element)
            overlapping = DetectCollision.find_collision(element, obstacles)
            self.remove_powerups(overlapping)
            element.update()
            if element.get_rect().right < 0:
                self.powerups_displayed.remove(element)

    def update_speed(self, speed):
        for element in self.powerups_displayed:
            element.set_speed(speed)
