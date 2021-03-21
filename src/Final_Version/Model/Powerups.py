import pygame
import random
import sys
sys.path.insert(1, '../View')
import LoadAssets

class Powerups(pygame.sprite.Sprite):
    def __init__(self, screen, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen 
        self.name = random_name()
        self.width = width
        self.height = height
        assets = LoadAssets.LoadAssets()
        self.image = pygame.transform.scale(assets.load_all_powerups()[self.name], (width, height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom - 100
        self.speed = speed

    # Private method
    def get_rect(self):
        return self.rect

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
        self.rect = self.rect.move([self.speed,0]) 

def random_name():
    i = random.randint(0,3)
    return i