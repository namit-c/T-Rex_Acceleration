import random
import sys
import pygame
import time
sys.path.insert(1, '../Model')
from Powerups import *

class DisplayPowerups():
    def __init__(self, game_screen):
        if (game_screen is None):
            raise Exception("IllegalArguemntException")
        self.game_screen = game_screen
        self.powerups_displayed = pygame.sprite.Group()
        self.__generate_time = time.time()
    def get_powerups_list(self):
        return self.powerups_displayed
    def remove_powerups(self, p):
        self.powerups_displayed.remove(p)
    def generate_powerups(self, speed):
        if (time.time() >= self.__generate_time + random.randint(3,5) and random.random() < 0.01):
            new_powerups = Powerups(self.game_screen, 50, 50, speed)
            self.powerups_displayed.add(new_powerups)
            self.__generate_time = time.time()
    def draw_powerups(self, powerups):
        self.game_screen.blit(powerups.get_img(), powerups.get_rect())
    def update_powerups(self):
        for element in self.powerups_displayed:
            self.draw_powerups(element)
            element.update()
