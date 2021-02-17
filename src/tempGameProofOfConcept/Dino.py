import pygame
from time import *

class Dino():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('Dino.png'), (75, 75))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + 100
        self.rect.bottom = self.screen_rect.bottom - 40
        self.isDucking = False
        self.isJumping = False
        self.isDead = False
        self.isInvincible = False
        self.movement = [0,0]
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def duck(self):
        if self.isJumping == False:
            self.isDucking = True
            self.image = pygame.transform.scale(pygame.image.load('Dino.png'), (85, 35))
            self.rect = self.image.get_rect()
            self.rect.bottom = self.screen_rect.bottom - 40
            self.rect.left = self.screen_rect.left + 100
    def stand(self):
        if self.isJumping == False:
            self.isDucking = False
            self.image = pygame.transform.scale(pygame.image.load('Dino.png'), (75, 75))
            self.rect = self.image.get_rect()
            self.rect.bottom = self.screen_rect.bottom - 40
            self.rect.left = self.screen_rect.left + 100
    def jump(self):
        if self.isJumping == False and self.isDucking == False:
            self.isJumping = True
            self.movement[1] = -20
    def checkbounds(self):
        if self.rect.bottom > self.screen_rect.bottom - 40:
            self.rect.bottom = self.screen_rect.bottom - 40
            self.isJumping = False
    def dead(self):
        self.isDead = True
    def invincible(self):
        self.isInvincible = True
        sleep(5)
        self.isInvincible = False
    def update(self):
        if self.isJumping:
            self.movement[1] += 1
        self.rect = self.rect.move(self.movement)   
        self.checkbounds()
