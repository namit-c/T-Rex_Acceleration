import pygame
import random

class Powerups(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, speed, powerup_img):
        pygame.sprite.Sprite.__init__(self)
        if (powerup_img is None):
            raise Exception("IllegalArguementException")
        self.screen = screen 
        self.image = powerup_img
        self.width = width
        self.height = height
        self.name = random_name()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + 500
        self.rect.bottom = self.screen_rect.bottom - 80
        self.speed = speed
    def get_width(self):
        return self.width
    def set_width(self, new_width):
        if (new_width < 0):
            raise Exception("IllegalArgumentException")
        self.width = new_width
    def get_height(self):
        return self.height
    def set_height(self, new_height):
        if (new_height < 0):
            raise Exception("IllegalArgumentException")
        self.height = new_height
    def get_speed(self):
        return self.width
    def set_speed(self, new_speed):
        self.speed = new_speed
    def get_img(self):
        return self.image
    def set_image(self, new_powerup_img):
        if (new_powerup_img is None):
            raise Exception("IllegalArgumentException")
        self.image = new_powerup_img
    def get_name(self):
        return self.name   
    def update(self):
        self.rect = self.rect.move([self.movement,0]) 

def random_name():
    i = random.randint(0,3)
    powerup_list = ["Invincibility", "Double Jump", "Score Boost", "Slo_mo"]
    return powerup_list[i]